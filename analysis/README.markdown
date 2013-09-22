
# Analysis

Use this area to analyze/document things in markdown.

Dumping binary logs to hex/markdown is a nice way to easily get
colorized diffs that are very useful to look at differences between
test runs.  This is extremely helpful when analyzing lots of data.


#### CSV exports from MM

```bash
$ ls analysis/*/*.csv
analysis/bewest-pump/bewest-carelink-spring-2013.csv
analysis/bewest-pump/bewest-pump-2010-02.csv
analysis/bewest-pump/bewest-pump-2010-05.csv
analysis/bewest-pump/bewest-pump-2010-08.csv
analysis/bewest-pump/bewest-pump-2010-10.csv
analysis/bewest-pump/bewest-pump-2011-01.csv
analysis/bewest-pump/bewest-pump-2011-04.csv
analysis/bewest-pump/bewest-pump-2011-06.csv
analysis/bewest-pump/bewest-pump-2011-09.csv
analysis/bewest-pump/bewest-pump-2011-12.csv
analysis/bewest-pump/bewest-pump-2012-02.csv
analysis/bewest-pump/bewest-pump-2012-05.csv
analysis/bewest-pump/bewest-pump-2012-08.csv
analysis/bewest-pump/bewest-pump-2012-10.csv
analysis/bewest-pump/bewest-pump-2013-01.csv
analysis/bewest-pump/Carelink-bewest-fall-2013.csv
analysis/ianj/codes_with_Ian.csv
analysis/sarak/CareLink-Export-1378424556878.csv
analysis/test-2000/Carelink-tester-208850-2000-01.csv
analysis/test-2004/Carelink-tester-2004-01-03.csv
analysis/tester-2012-08/Carelink-208850-2012-08.csv

```

Basic idea is that these csv records should line up with the records we can
decode from the binary files.


#### `analysis/`
```csv
analysis/389877,aka europe-722
analysis/047006,aka xiali
analysis/511999,aka sarak
analysis/665455,aka bewest-pump
analysis/720726,aka ianj
analysis/208850,aka tester
```


## how to run analysis

This example created a
[commit](https://github.com/bewest/decoding-carelink/tree/master/analysis/047006)
with
[these results](https://github.com/bewest/decoding-carelink/tree/master/analysis/047006).

```bash
# look at download.log to get serial number (optional)
tail analysis/xiali/raw/download.log 
# 
export SERIAL=047006
set_tool_args ""
# by default, run_regress will attempt to decode everything in ./logs/*.data
run_regress analysis/xiali/raw/
git status
git diff
git status
git commit  -av
git push origin 

```


### xiali

```bash
tail analysis/xiali/raw/download.log 
export SERIAL=047006
set_tool_args ""
run_regress analysis/xiali/raw/
git status
git diff
git status
git commit  -av
git push origin 

```

### bewest-pump

#### SERIAL `665455`
##### analysis/bewest-pump/Carelink-bewest-fall-2013.csv

```bash
$ tail analysis/bewest-pump/fall-2013/download.log 
    if command.done( ):
  File "/home/bewest/src/decoding-carelink/decocare/commands.py", line 218, in done
    self.eod  = eod = (self.data[5] & 0x80) > 0
IndexError: bytearray index out of range
Command exited with non-zero status 1
python decocare/download.py /dev/ttyUSB0 665455
        elapsed 2:13.82
        user 4.05
        system 0.58
        CPU 3% (0text+0data 59968max)k
bewest@paragon:~/src/decoding-carelink$ 

```
