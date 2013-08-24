# ./status-quo.sh /dev/ttyUSB0 047006
## cat ./status-quo.sh
```bash
```
## cat logs/explain.log
OUT
## Observations
Sat Aug 24 19:36:07 EDT 2013

## stick

* not ok

## pump


## downloaded: 0

```
```


## commands session:finished: 0

```
```

howdy! pump runs were NOT OK

### Last send command

```
```
### stats before traceback

```
```
### Traceback

```
echo "OUT" | tee logs/explain.log
. ./explain-brief.sh | tee -a logs/explain.log
explain_markdown


#####
# EOF
Sat Aug 24 19:36:06 EDT 2013
```
INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
Traceback (most recent call last):
  File "decocare/stick.py", line 854, in <module>
    stick = Stick(link.Link(port))
  File "/home/sharon/decoding-carelink/decocare/link.py", line 18, in __init__
    self.open( port )
  File "/home/sharon/decoding-carelink/decocare/link.py", line 27, in open
    self.serial = serial.Serial( self.port, **kwds )
  File "/usr/lib/python2.7/dist-packages/serial/serialutil.py", line 260, in __init__
    self.open()
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 276, in open
    raise SerialException("could not open port %s: %s" % (self._port, msg))
serial.serialutil.SerialException: could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
Command exited with non-zero status 1
python decocare/stick.py /dev/ttyUSB0
	elapsed 0:00.27
	user 0.09
	system 0.02
	CPU 44% (0text+0data 59296max)k
```
```
INFO:__main__:howdy! I'm going to take a look at your pump.
Traceback (most recent call last):
  File "decocare/session.py", line 123, in <module>
    stick = stick.Stick(link.Link(port, timeout=.200))
  File "/home/sharon/decoding-carelink/decocare/link.py", line 18, in __init__
    self.open( port )
  File "/home/sharon/decoding-carelink/decocare/link.py", line 27, in open
    self.serial = serial.Serial( self.port, **kwds )
  File "/usr/lib/python2.7/dist-packages/serial/serialutil.py", line 260, in __init__
    self.open()
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 276, in open
    raise SerialException("could not open port %s: %s" % (self._port, msg))
serial.serialutil.SerialException: could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
Command exited with non-zero status 1
python decocare/session.py /dev/ttyUSB0 047006
	elapsed 0:00.12
	user 0.08
	system 0.01
	CPU 81% (0text+0data 59376max)k
```
```
INFO:__main__:howdy! I'm going to take a look at your pump and grab lots of info.
Traceback (most recent call last):
  File "decocare/commands.py", line 646, in <module>
    stick = stick.Stick(link.Link(port, timeout=.400))
  File "/home/sharon/decoding-carelink/decocare/link.py", line 18, in __init__
    self.open( port )
  File "/home/sharon/decoding-carelink/decocare/link.py", line 27, in open
    self.serial = serial.Serial( self.port, **kwds )
  File "/usr/lib/python2.7/dist-packages/serial/serialutil.py", line 260, in __init__
    self.open()
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 276, in open
    raise SerialException("could not open port %s: %s" % (self._port, msg))
serial.serialutil.SerialException: could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
Command exited with non-zero status 1
python decocare/commands.py /dev/ttyUSB0 047006
	elapsed 0:00.14
	user 0.10
	system 0.02
	CPU 82% (0text+0data 60976max)k
```
Was there an ACK ERROR?
### DIAGNOSE CRC
```
INFO:__main__:howdy! I'm going to take a look at your carelink usb stick.
Traceback (most recent call last):
  File "decocare/stick.py", line 854, in <module>
    stick = Stick(link.Link(port))
  File "/home/sharon/decoding-carelink/decocare/link.py", line 18, in __init__
    self.open( port )
  File "/home/sharon/decoding-carelink/decocare/link.py", line 27, in open
    self.serial = serial.Serial( self.port, **kwds )
  File "/usr/lib/python2.7/dist-packages/serial/serialutil.py", line 260, in __init__
    self.open()
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 276, in open
    raise SerialException("could not open port %s: %s" % (self._port, msg))
serial.serialutil.SerialException: could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
Command exited with non-zero status 1
python decocare/stick.py /dev/ttyUSB0
	elapsed 0:00.11
	user 0.08
	system 0.03
	CPU 97% (0text+0data 59312max)k
```
```
INFO:__main__:howdy! I'm going to take a look at your pump download something info.
Traceback (most recent call last):
  File "decocare/download.py", line 78, in <module>
    stick = stick.Stick(link.Link(port, timeout=.400))
  File "/home/sharon/decoding-carelink/decocare/link.py", line 18, in __init__
    self.open( port )
  File "/home/sharon/decoding-carelink/decocare/link.py", line 27, in open
    self.serial = serial.Serial( self.port, **kwds )
  File "/usr/lib/python2.7/dist-packages/serial/serialutil.py", line 260, in __init__
    self.open()
  File "/usr/lib/python2.7/dist-packages/serial/serialposix.py", line 276, in open
    raise SerialException("could not open port %s: %s" % (self._port, msg))
serial.serialutil.SerialException: could not open port /dev/ttyUSB0: [Errno 2] No such file or directory: '/dev/ttyUSB0'
Command exited with non-zero status 1
python decocare/download.py /dev/ttyUSB0 047006
	elapsed 0:00.10
	user 0.08
```
* NO CRC ERROR FOUND
* no nak found
* NOT A CLEAN RUN
