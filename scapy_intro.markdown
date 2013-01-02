
# Help me learn scapy?

## What is all this?

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
