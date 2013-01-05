
# Basal Histories?

We think that the only difference between this run and the "rosetta"
run is the passing of time.  No bolus were given.  This means the only
new data in the logs should be basal histories.

No new data was found between these runs and the rosetta runs.
It appears state changes between basal rates while executing the basal
schedule are not written into the history pages.  As an editorial
note, we believe these changes are important and find it odd to
observe them missing.

BTW, running the carelink diagnostic software will write new entries
into the history log.

## Dumping Insulin Pump Memory

The pump command `ReadHistoryData` (`opcode 128`) dumps the pump's
memory.

The result piped through `od` looks like this:
Force everything to unsigned decimals, 8 at a time.

`od -t u1 --width=8`

### `od -t u1 --width=8 pages/binary-page-4.data`

```od

0000000 108  23 128   5  12   0 232   0
0000010   0   0   0   0   0   0   0   0
*
0000040   0   0   0   0   0   0   7   0
0000050   0   0   0  24 128 108  24 128
0000060   5  12   0 232   0   0   0   0
0000070   0   0   0   0   0   0   0   0
*
0000120   0   0   0   7   0   0   0   0
0000130  25 128 108  25 128   5  12   0
0000140 232   0   0   0   0   0   0   0
0000150   0   0   0   0   0   0   0   0
*
0000200   7   0   0   0   0  26 128 108
0000210  26 128   5  12   0 232   0   0
0000220   0   0   0   0   0   0   0   0
*
0000250   0   0   0   0   0   7   0   0
0000260   0   0  27 128 108  27 128   5
0000270  12   0 232   0   0   0   0   0
0000300   0   0   0   0   0   0   0   0
*
0000330   0   0   7   0   0   0   0  28
0000340 128 108  28 128   5  12   0 232
0000350   0   0   0   0   0   0   0   0
*
0000400   0   0   0   0   0   0   0   7
0000410   0   0   0   0  29 128 108  29
0000420 128   5  12   0 232   0   0   0
0000430   0   0   0   0   0   0   0   0
*
0000460   0   0   0   0   7   0   0   0
0000470   0  30 128 108  30 128   5  12
0000500   0 232   0   0   0   0   0   0
0000510   0   0   0   0   0   0   0   0
*
0000540   0   7   0   0   0   0  31 128
0000550 108  31 128   5  12   0 232   0
0000560   0   0   0   0   0   0   0   0
*
0000610   0   0   0   0   0   0   7   0
0000620   0   0   0  33   0 108  33   0
0000630   5  12   0 232   0   0   0   0
0000640   0   0   0   0   0   0   0   0
*
0000670   0   0   0   7   0   0   0   0
0000700  34   0 108  34   0   5  12   0
0000710 232   0   0   0   0   0   0   0
0000720   0   0   0   0   0   0   0   0
*
0000750   7   0   0   0   0  35   0 108
0000760  35   0   5  12   0 232   0   0
0000770   0   0   0   0   0   0   0   0
*
0001020   0   0   0   0   0   7   0   0
0001030   0   0  36   0 108  36   0   5
0001040  12   0 232   0   0   0   0   0
0001050   0   0   0   0   0   0   0   0
*
0001100   0   0   7   0   0   0   0  37
0001110   0 108  37   0   5  12   0 232
0001120   0   0   0   0   0   0   0   0
*
0001150   0   0   0   0   0   0   0   7
0001160   0   0   0   0  38   0 108  38
0001170   0   5  12   0 232   0   0   0
0001200   0   0   0   0   0   0   0   0
*
0001230   0   0   0   0   7   0   0   0
0001240   0  39   0 108  39   0   5  12
0001250   0 232   0   0   0   0   0   0
0001260   0   0   0   0   0   0   0   0
*
0001310   0   7   0   0   0   0  40   0
0001320 108  40   0   5  12   0 232   0
0001330   0   0   0   0   0   0   0   0
*
0001360   0   0   0   0   0   0   7   0
0001370   0   0   0  41   0 108  41   0
0001400   5  12   0 232   0   0   0   0
0001410   0   0   0   0   0   0   0   0
*
0001440   0   0   0   7   0   0   0   0
0001450  42   0 108  42   0   5  12   0
0001460 232   0   0   0   0   0   0   0
0001470   0   0   0   0   0   0   0   0
*
0001520   7   0   0   0   0  43   0 108
0001530  43   0   5  12   0 232   0   0
0001540   0   0   0   0   0   0   0   0
*
0001570   0   0   0   0   0   7   0   0
0001600   0   0  44   0 108  44   0   5
0001610  12   0 232   0   0   0   0   0
0001620   0   0   0   0   0   0   0   0
*
0001650   0   0   7   0   0   0   0  45
0001660   0 108  45   0   5  12   0 232
0001670   0   0   0   0   0   0   0   0
*
0001720   0   0   0   0   0   0   0   7
0001730   0   0   0   0  46   0   0   0
0001740   0   0   0   0   0   0   0   0
*
0001770   0   0   0   0   0   0 179 216
0002000

```

