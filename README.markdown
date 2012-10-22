
# Decoding carelink

For an intro, see
[insulaudit](https://github.com/bewest/insulaudit/tree/master/questions).

## Data

* `./CareLink-Export-1350867079937.csv` - One day of "use" manipulating lots of
  settings.
* `./first_run.csv`  - Interogate basic settings
* `./second_run.csv` - Add more basals, quick bolus
* `./third_run.csv`  - More bolus

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

### 

