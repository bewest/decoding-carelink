
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

All the output from CSV and `list_dates.py`


