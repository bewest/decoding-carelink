
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

### What is all this?

We're working with [insulaudit](https://github.com/bewest/insulaudit),
a python library to audit and interrogate medical devices.  The
protocols that govern our insulin pumps are locked, ensuring incorrect
therapy without recourse.  Meanwhile adverse events are attributed to
"user-error."

Now that I'm a bit more familiar with how the
[basic model works](https://github.com/bewest/decoding-carelink/wiki/Sequencediagram), I was hoping to use scapy to round out the corners.
[see decoder.py](https://github.com/bewest/decoding-carelink/blob/master/decoder.py)

But I could use a few pointers in the right direction.  I've been
reading through some other protocols:

* https://github.com/jwiegley/scapy/blob/master/scapy/layers/llmnr.py
* https://github.com/moros/osmocombb-scapy/blob/master/l1ctl.py
* http://stackoverflow.com/questions/7897522/building-scapy-packets-with-packetfields-shorter-than-8-bits
* http://www.secdev.org/projects/scapy/doc/build_dissect.html#simple-example
* http://stackoverflow.com/questions/10556593/obtaining-field-types-dynamically-according-to-a-field-from-another-class-using?rq=1
* http://stackoverflow.com/questions/6572253/scapy-independant-layers-no-encapsulation?rq=1
* http://stackoverflow.com/questions/11929133/new-protocol-layer-for-scapy

Plus reading through scapy sources, the `ASN.1`, stuff, and looking at how
bind_layers works.

It appears to me as if multiple requests are required for one logical
fetch of information, and I'm wondering how to build this up in scapy.

One kind of mega-model that attempts to sniff for context, or is there
a clever way to do this with thin wrappers that bind correctly
depending on the context?

It's important to note, I can identify most of the bytes involved
here:
* https://github.com/bewest/insulaudit/blob/master/cl2.py
* https://github.com/bewest/insulaudit/blob/master/src/insulaudit/clmm/usbstick.py

The big problem is that we cannot interpret the actual contents from
the payloads.  However, the captures in decoding-carelink are 100%
under my control, with data entered by me, constrained to a single
day.  And we have made some progress in identifying some of the
contents: [php analysis](https://gist.github.com/3860720)

So the task immediately before me, I suppose is to patch the tool so
that it produces packets of command requests and the payload contents
for further analysis?

Any pointers, help patching MUCH appreciated.
Thanks,
-[contributors](https://github.com/bewest/decoding-carelink/network/members)

