
# Decoding carelink

For an intro, see
[insulaudit](https://github.com/bewest/insulaudit/tree/master/questions).
We are hoping to help diabetics independently reproduce therapeutic
audits of their Medtronic insulin pumps.  This experimental software
will download pump settings, and the entire log of historical data.

## [Docs](http://bewest.github.io/decoding-carelink/)

Spot something incorrect or not working?  Want a feature/tool to do
something?
[Please file an issue!](https://github.com/bewest/decoding-carelink/issues)

* http://bewest.github.io/decoding-carelink/ Sphinx docs.
* https://gist.github.com/bewest/6330546 some diagrams

![overview](https://gist.github.com/bewest/6330546/raw/dffdb1e95ef9882e3929579784f95db8c5c6705d/overview.seq.png)

## Status

We can decode many of the opcodes that store configuration settings.
We can also download all pages of history from the ReadHistoryData
command, which contains the log of all actions the pump has taken on
your behalf:

* glucose readings
* all bolus dosings, all usage of bolus wizard
* unabsorbed insulin
* alarms, etc...
* current settings
* query pump status: normal, suspended, bolusing
  `./bin/mm-set-suspend.py`
* set/edit/query temporary basal rates
  `./bin/set_temp_rate.py`
* press any button on the keypad, using
  `./bin/mm-press-key.py`

## Install first run

This only needs to be done once:

```bash
git clone https://github.com/bewest/decoding-carelink.git
cd decoding-carelink
sudo python ez_setup.py # only if you rarely use python
sudo python setup.py develop
git checkout -b myname/init # replace <myname> with your name
# all done
```

Congratulations, now you are ready for the demo:
Plug in the carelink usb stick, and run this:
```bash
dmesg | grep ttyUSB # notice the new ttyUSB$x
sudo ./insert.sh
```

You are all done with setup.
Here's how to test just the usb stick, then we'll run the full suite of
experiments.

* on **MAC** the `PORT` is called `/dev/tty.serial` or something.
* on **windows** the `PORT` is called `COM1` or something
* on **Linux** the `PORT` is called `/dev/ttyUSBx` or something

```bash
python decocare/stick.py /dev/ttyUSB0 # on windows this is called COM1
# should get a bunch of output, notably some counters called INTERFACE STATS
# run all experiments:
./status-quo.sh /dev/ttyUSB0 <pump-serial> # use your pump's serial number
```

Fantastic.
Send me your results!

Do this every time, after you run some experiments:
```bash
git commit -avm 'for @bewest, these are @<my-name> results'
```

Set up for sending me results.
```bash
# email me your results like this:
git bundle create myname-expr.bundle master..myname/init
# you can send me myname-expr.bundle in an email
```

Even better, [fork the repo](https://github.com/bewest/decoding-carelink/fork)
and setup to for easy.
```bash
# add your fork like this:
git remote rename origin author
git remote add origin git@github.com:<my-user-name>/decoding-carelink.git
git push -u origin myname/init
```


Now you can do this easily:
```bash
./status-quo.sh /dev/ttyUSB0 <pump-serial> # use your pump's serial number
git commit -avm 'for @bewest, these are @<my-name> results'
git push -u origin myname/init
```

Repeat.  The easiest way to see what happened is to look at
explain.log, and use `git diff` and `git show`.  Pushing to github as
shown above will allow everyone to discuss our analysis together.

There are several log files created for each experiment.


## Demo

> If you don't want to use your own equipment, I've made some of my
> test equipment available.
Talk to my test insulin pump over the internet.

Requires `socat` and `python 2.7`.  The script [`./bin/socat_run_app.sh`](https://github.com/bewest/decoding-carelink/blob/master/bin/socat_run_app.sh)
will connect to my server, `bewest.io:8080` where my test insulin
pump, serial `208850` is waiting to talk to you.

Here's an example using my scripts:

```bash
$ git checkout -b tester # create a new branch with just your stuff, please
$ . ./bin/common # import some handy run_* functions
$ ./bin/socat_run_app.sh & # get my test insulin pump from bewest.io:8080
$ ls carelink.ttyUSB0  # creates this thing
carelink.ttyUSB0
$ ./status-quo.sh ./carelink.ttyUSB0
[...]
$ PORT=./carelink.ttyUSB0 SERIAL=208850 run_download 
[...]

```
* [download](https://raw.github.com/bewest/decoding-carelink/tester/logs/download.log)
* [commands](https://github.com/bewest/decoding-carelink/blob/tester/logs/commands.log)

Try figuring out the dosing commands.  Is it possible to rewind
the pump?  Is it possible to enter new profiles and schedules?

## Future work

* collect more data
* finish [analyzing pages of insulin pump history](https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/pages.markdown)
* https://github.com/bewest/decoding-carelink/tree/rewriting/analysis/pages
** [analyze insulin pump bolus records](https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/bolus.markdown)
** [help analyze prime events](https://github.com/bewest/decoding-carelink/blob/rewriting/ground-start-0/decoding-prime-events.markdown)
** [help analyze pump midnight events](https://github.com/bewest/decoding-carelink/tree/rewriting/basal-hist-2006)

Once we can decode historical logs, we'll clean up and merge back into
[insulaudit](https://github.com/bewest/insulaudit/tree/master/hacking)

### Help needed

Documentation of protocol, decoders, etc...

```bash
# fork the repo on github
# clone the repo
$ git clone git@github.com/<yourname>/decoding-carelink.git
$ cd decoding-carelink
$ git checkout -b <yourname>
$ ./insert.sh # will ask for sudo to configure usbserial for the stick
# ./status-quo.sh [[<path>|/dev/ttyUSB0>] [<serial>|208850]] eg:
$ ./status-quo.sh /dev/ttyUSB0 208850
$ git commit -avm "here is my data <yourname>"
$ git push -u origin <yourname>
```
Thanks!
If you can include CSV export from carelink, it would be helpful.

### Decoding

We know how to
[decode time](https://github.com/bewest/decoding-carelink/blob/master/new-years-day/rollover-month/stage-5.markdown)
and as a result we can find and parse most records now.

And lining this up with the Carelink CSV exports reveals the nature of
the contents for further analysis.

Once we can decode all records, it should be useful for
diabetics, to get basic reports, more or less on par with the
vendor's solution.
We'll use it to 
[collect diabetes data](https://github.com/bewest/insulaudit/tree/master/hacking)
(https://github.com/bewest/decoding-carelink/tree/rewriting/analysis/pages)
over the internet, allowing anyone to independently audit their
therapy, and then send the data to their preferred auditing software.

## Tools
### `./bin/set_temp_rate.py`

```bash
usage: set_temp_rate.py [-h] [--serial SERIAL] [--port PORT]
                        [--duration DURATION] [--rate RATE]

optional arguments:
  -h, --help           show this help message and exit
  --serial SERIAL      serial number of pump [default: ]
  --port PORT          Path to device [default: ]
  --duration DURATION  Duration of temp rate [default: 0)]
  --rate RATE          Rate of temp basal [default: 0)]
```

Eg:

`./bin/set_temp_rate.py --duration 60 --rate 2.0`

**Duration** is in minutes, must be in 30 minute intervals!
**Rate** is float, describing units per hour.  Smallest rate is
`0.025`, and increments by that mount.

### `./bin/mm-set-suspend.py`

```bash
usage: mm-set-suspend.py [-h] [--serial SERIAL] [--port PORT] [--no-op] [-v]
                         [--init]
                         {query,suspend,resume} [{query,suspend,resume} ...]

positional arguments:
  {query,suspend,resume}
                        Set or query pump status [default: query)]

optional arguments:
  -h, --help            show this help message and exit
  --serial SERIAL       serial number of pump [default: ]
  --port PORT           Path to device [default: ]
  --no-op               Dry run, don't do main function
  -v, --verbose         Verbosity
  --init                Send power ctrl to initialize RF session.
```

#### `./bin/mm-press-key.py`

```bash
usage: mm-press-key.py [-h] [--serial SERIAL] [--port PORT] [--no-op] [-v]
                       [--init]
                       {act,esc,up,down,easy} [{act,esc,up,down,easy} ...]

positional arguments:
  {act,esc,up,down,easy}
                        buttons to press [default: act)]

optional arguments:
  -h, --help            show this help message and exit
  --serial SERIAL       serial number of pump [default: ]
  --port PORT           Path to device [default: ]
  --no-op               Dry run, don't do main function
  -v, --verbose         Verbosity
  --init                Send power ctrl to initialize RF session.
```

#### `status-quo.sh`

`status-quo.sh </dev/ttyUSB0> <SERIAL>` runs several experiments, described below.
Each experiment is saved in the `./logs` directory, which is tracked by git.


##### `. bin/common`
Source a bunch of helper functions, notably:

##### `run_stick`_
Runs `python decocare/stick.py /dev/ttyUSB0`
and saves results in `logs/stick.log`.
When run by `status-quo.sh`, it creates
`./logs/baseline.stick.log` before continuing.
At end of experiments, it records `./logs/postmortem.stick.log`

##### `run_session`_
Runs `python decocare/session.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/session.log`.

##### `run_commands`_
Runs `python decocare/commands.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/commands.log`.

##### `run_download`_

Runs `python decocare/download.py /dev/ttyUSB0 <SERIAL>`
and saves results in `logs/download.log`.

The download script is configured to save each page of historical data as a raw
binary blob in the `./logs/` subdirectory like this:
`./logs/ReadHistoryData-page-$x.data`.

This script can take several minutes to run; it attempts to download
all pages of data available.

#### quick overview:

`status-quo.sh` also tries to summarize what happened, saving a quick
explanation of what happened in `logs/explain.log`.  The entire output
is saved in `./status-quo.log`.

#### `run_regress`
After `. bin/common`, `export SERIAL=511888` with your serial number.

Runs `python list_history.py` on each binary file found in `logs/`, saves
results in `./analysis/<SERIAL>/...`.

This is what I use to render the markdown files in analysis.
Often, the diffs between runs help test theories.

#### `list_history.py`
`list_history.py [--larger] ./logs/ReadHistory....page-0.data`
List/decode a page of history as markdown.

#### `list_opcodes.py`
`list_opcodes.py`
List records found in binary data by looking for opcodes, and a
regular data structure associated with that length.  Includes at least
one variable stop length strength.

#### `list_dates.py`
List records found in binary data by looking for dates.

#### usblyzer_filter.sh

```bash
# usblyzer_filter.sh was used to filter the raw usblyzer csv export into
# something a bit more manageable.
$ history
  553  ./usblyzer_filter.sh  first_run.csv  
  554  ls
  555  git mv first_run.csv pcaps/first_run/
  556  ./usblyzer_filter.sh  pcaps/first_run/first_run.csv  
  557  ./usblyzer_filter.sh  pcaps/first_run/first_run.csv   > pcaps/first_run/pcap.csv
  558  git mv second_run.csv pcaps/second_run/
  559  ./usblyzer_filter.sh pcaps/second_run/second_run.csv 
  560  ./usblyzer_filter.sh pcaps/second_run/second_run.csv  > pcaps/second_run/pcap.csv
  561  git mv third_run.csv pcaps/third_run/
  562  ./usblyzer_filter.sh  pcaps/third_run/third_run.csv 
  563  ./usblyzer_filter.sh  pcaps/third_run/third_run.csv  > pcaps/third_run/pcap.csv
bewest@paragon:~/src/decoding-carelink$ 
```

Thanks,
-[contributors](https://github.com/bewest/decoding-carelink/network/members)

