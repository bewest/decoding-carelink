
# Decoding carelink

For an intro, see
[insulaudit](https://github.com/bewest/insulaudit/tree/master/questions).

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

## Future work

* collect more data

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

## Data

* pcaps/
  * `./CareLink-Export-1350867079937.csv` - One day of "use" manipulating lots of
    settings.
  * `./first_run.csv`  - Interogate basic settings
  * `./second_run.csv` - Add more basals, quick bolus
  * `./third_run.csv`  - More bolus
* history/ - some experiments to get any historical data out of a pump 
* rosetta-july-1-2006 - some initial experiments to perform some
  activities on the pump and observe changes to the memory dump of the
  pump
* basal-hist-2006 - a kind of baseline memory dump the day after
  rosetta-july-1-2006 activities.
* ground-start-0 - starting to get pretty rigorous about noticing
  differences between memory dumps, and isolating various pump
  activities
* new-years-day - carefully isolate activities and changes in the
  memory dump.  See the different stages to watch what happens to the
  memory as we isolate each activitiy.  Stage-5 results in being able
  to read the date-times out of the binary logs.

## Tools

#### hexlog2binary.sh
Convert a hexdump from cl2.py into binary data.
Used something like:

```bash
function new_name ( ) { echo $1 | sed -e "s/hex/binary/g" | sed -e "s/log/data/g"; }

bewest:~/src/decoding-carelink/new-years-day/rollover-month/stage-5$ for x in hex-*; do ../../../hexlog2binary.sh  $x $(new_name $x); done
```

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

