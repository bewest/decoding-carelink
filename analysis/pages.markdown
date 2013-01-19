
# what do pages look like?

So, the `ReadHistoryData`, `opcode 128` is special.
The response is 1024 bytes.  Oh, and they are organized into something
called `pages`.  It seems to contain a log of the pump's core
behavior over time.  Fantastic!

Using the knowledge we gleaned from reading time, we built a basic
parser, `list_dates.py` which reads a binary file, one byte at a time,
until it finds a valid date.  By tweaking the behavior of this parser
over time, regular output began to emerge, especially from page 1.

It turns out that by comparing page 1 to a CSV output, almost every
record began to pop out.

## bolus records

* https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/bolus.markdown
* https://github.com/bewest/decoding-carelink/tree/rewriting/ground-start-0

## rewind/prime records

* https://github.com/bewest/decoding-carelink/blob/rewriting/ground-start-0/decoding-prime-events.markdown
* https://github.com/bewest/decoding-carelink/tree/rewriting/ground-start-0
* https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/prime-rewind.markdown

## midnight

The midnight record is the hardest.

* https://github.com/bewest/decoding-carelink/tree/rewriting/basal-hist-2006
This particular hex dump is full of midnight records.

## all output
* https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/tester-2006-07.markdown

All the output from CSV and `list_dates.py`.

Here's a useful synopsis I like of `list_dates.py`:
```bash
python list_dates.py logs/ReadHistoryData-page-0.data logs/ReadHistoryData-page-1.data logs/ReadHistoryData-page-2.data logs/ReadHistoryData-page-3.data logs/ReadHistoryData-page-4.data logs/ReadHistoryData-page-5.data logs/ReadHistoryData-page-6.data logs/ReadHistoryData-page-7.data logs/ReadHistoryData-page-8.data
```

```
logs/ReadHistoryData-page-0.data: 13 records
RECORD 0: 2006-10-04T08:00:19 0x07 hex(47), extra(0)
RECORD 1: 2003-08-06T04:40:11 0x03 hex(6), extra(4)
RECORD 2: 2007-08-06T04:08:11 0x9e hex(1), extra(0)
RECORD 3: 2012-06-05T06:36:44 0x00 hex(6), extra(0)
RECORD 4: 2012-06-05T06:37:44 0x00 hex(40), extra(0)
RECORD 5: 2012-06-05T06:38:44 0x00 hex(40), extra(0)
RECORD 6: 2006-10-07T23:01:00 0x00 hex(35), extra(0)
RECORD 7: 2006-10-08T20:31:03 0x07 hex(47), extra(0)
RECORD 8: 2006-10-08T20:31:46 0x1a hex(2), extra(0)
RECORD 9: 2012-06-05T06:41:44 0x07 hex(52), extra(0)
RECORD 10: 2012-06-05T06:42:44 0x00 hex(40), extra(0)
RECORD 11: 2006-10-11T16:48:45 0x00 hex(35), extra(0)
RECORD 12: 2006-10-12T07:55:42 0x07 hex(47), extra(0)
logs/ReadHistoryData-page-1.data: 45 records
RECORD 0: 2006-07-01T08:23:47 0x5b hex(2), extra(22)
RECORD 1: 2006-07-01T08:24:43 0x5b hex(2), extra(22)
RECORD 2: 2006-07-01T08:26:55 0x6b hex(7), extra(27)
RECORD 3: 2006-07-01T08:36:21 0x1e hex(2), extra(0)
RECORD 4: 2006-07-01T08:36:43 0x1f hex(2), extra(0)
RECORD 5: 2011-08-12T00:36:16 0x07 hex(29), extra(0)
RECORD 6: 2006-07-02T18:29:32 0x01 hex(13), extra(0)
RECORD 7: 2006-07-02T18:30:24 0x1f hex(2), extra(0)
RECORD 8: 2006-07-02T18:37:23 0x1e hex(2), extra(0)
RECORD 9: 2006-07-02T18:37:41 0x1f hex(2), extra(0)
RECORD 10: 2006-07-02T18:57:35 0x1e hex(2), extra(0)
RECORD 11: 2006-07-02T18:58:58 0x1f hex(2), extra(0)
RECORD 12: 2006-07-03T10:00:14 0x07 hex(47), extra(0)
RECORD 13: 2006-07-03T10:00:32 0x1f hex(2), extra(0)
RECORD 14: 2006-07-06T15:12:00 0x07 hex(137), extra(0)
RECORD 15: 2006-07-07T02:30:01 0x07 hex(47), extra(0)
RECORD 16: 2006-07-07T15:05:03 0x5b hex(2), extra(22)
RECORD 17: 2006-07-07T16:14:05 0x5b hex(2), extra(22)
RECORD 18: 2006-07-07T16:47:57 0x45 hex(7), extra(6)
RECORD 19: 2006-07-07T16:49:12 0xf0 hex(9), extra(0)
RECORD 20: 2006-07-07T17:10:38 0x03 hex(5), extra(4)
RECORD 21: 2006-07-07T17:28:51 0x03 hex(1), extra(4)
RECORD 22: 2006-07-07T17:41:14 0x03 hex(1), extra(4)
RECORD 23: 2006-07-07T17:57:02 0x03 hex(1), extra(4)
RECORD 24: 2006-07-07T18:02:05 0x03 hex(1), extra(4)
RECORD 25: 2006-07-07T18:22:51 0x12 hex(5), extra(0)
RECORD 26: 2006-07-08T05:22:49 0x07 hex(50), extra(0)
RECORD 27: 2006-07-08T05:49:07 0x1e hex(2), extra(0)
RECORD 28: 2006-07-08T05:49:26 0x1f hex(2), extra(0)
RECORD 29: 2006-07-08T07:11:37 0x64 hex(2), extra(0)
RECORD 30: 2006-07-08T07:12:12 0x17 hex(2), extra(0)
RECORD 31: 2006-08-15T23:30:00 0x18 hex(2), extra(0)
RECORD 32: 2006-08-15T23:33:28 0x07 hex(50), extra(0)
RECORD 33: 2006-08-15T23:33:54 0x03 hex(5), extra(4)
RECORD 34: 2006-08-15T23:34:28 0x03 hex(1), extra(4)
RECORD 35: 2012-06-05T06:31:44 0x06 hex(3), extra(0)
RECORD 36: 2006-09-01T00:12:41 0x00 hex(38), extra(0)
RECORD 37: 2006-09-01T00:44:29 0x1e hex(2), extra(0)
RECORD 38: 2006-09-01T00:44:48 0x1f hex(2), extra(0)
RECORD 39: 2006-09-01T01:19:10 0x64 hex(2), extra(0)
RECORD 40: 2006-09-01T01:19:34 0x17 hex(2), extra(0)
RECORD 41: 2006-10-01T11:20:00 0x18 hex(2), extra(0)
RECORD 42: 2006-10-01T11:30:18 0x07 hex(50), extra(0)
RECORD 43: 2006-10-02T19:45:47 0x07 hex(47), extra(0)
RECORD 44: 2006-10-03T13:09:13 0x07 hex(47), extra(0)
logs/ReadHistoryData-page-2.data: 73 records
RECORD 0: 2012-08-01T21:28:39 0x03 hex(15), extra(4)
RECORD 1: 2012-08-01T22:25:34 0x16 hex(19), extra(0)
RECORD 2: 2012-08-01T22:31:47 0x27 hex(16), extra(0)
[...]
```

And it goes on to be mostly wrong.  Page 1 is exceptional.  It has
confirmed bolus records, reproduced in every analysis.  The
`list_dates.py`_ technique falls over whenever the the run
`0x07 0x00 0x00 0x??` is found, with what looks like a date.  If not
capped, it will eat the next event's date.  If capped the parser gets
thrown off the tracks.

The analysis so far does seem to indicate a basic record structure
that looks like this:
```
HEAD - two bytes?
[ opcode,  param? ]
DATETIME
[sec, min, hour, day, year ]
BODY
[??]

```

The byte for byte approach needs some additional rules.


