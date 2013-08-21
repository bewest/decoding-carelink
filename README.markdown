
# Decoding carelink

For an intro, see
[insulaudit](https://github.com/bewest/insulaudit/tree/master/questions).
We are hoping to help diabetics independently reproduce therapeutic
audits of their Medtronic insulin pumps.  This experimental software
will download pump settings, and the entire log of historical data.

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

## Install first run:

This only needs to be done once:

```bash
git clone https://github.com/bewest/decoding-carelink.git
cd decoding-carelink
sudo python ez_setup.py # only if you rarely use python
sudo python setup.py develop
git checkout -b myname/init
# all done

```
Now you are ready for the demo:

```bash
$ . ./bin/common # import some handy run_* functions
$ dmesg | grep ttyUSB # notice the path to the new ttyUSB$x
$ sudo ./insert.sh
$ ./status-quo.sh /dev/ttyUSB0

```

## Demo

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

#### hexlog2binary.sh
Convert a hexdump from cl2.py into binary data.
Used something like:

```bash
function new_name ( ) { echo $1 | sed -e "s/hex/binary/g" | sed -e "s/log/data/g"; }

bewest:~/src/decoding-carelink/new-years-day/rollover-month/stage-5$ for x in hex-*; do ../../../hexlog2binary.sh  $x $(new_name $x); done
```

#### list_opcodes.py
List records found in binary data by looking for opcodes, and a
regular data structure associated with that length.  Includes at least
one variable stop length strength.

#### list_dates.py
List records found in binary data by looking for dates.

#### cl2.py
Download data from an insulin pump.
[cl2.py src](https://github.com/bewest/insulaudit/blob/master/cl2.py)
Working on a simpler version...

Covers about a dozen opcodes, including downloading multiple "pages"
of historical data from a pump.

#### decoder.py
Run a binary file through a rudimentary scapy model.

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

