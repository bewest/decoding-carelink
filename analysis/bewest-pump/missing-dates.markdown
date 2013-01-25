### analysis/bewest-pump/ReadHistoryData-page-0.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-10.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-11.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-12.data.list_opcodes.markdown
WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-12.data
#### RECORD 0 BolusGiven? 2010-12-26T01:20:30 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x0b 0x14 0x08 0x04 0x06 0xd4 0x14    \.......
    0008   0x92                                       .
    decimal
             92   11   20    8    4    6  212   20
            146
    datetime (2010-12-26T01:20:30)
    0000   0xde 0x14 0x01 0x3a 0x3a                   ...::
    body (0)
    DAY BITS: [0, 0, 1] YEAR BITS: [0, 0, 1, 1]

#### RECORD 1 Record 2014-01-12T10:03:52 head[2], body[0] 0x00
    op hex (2)
    0000   0x00 0xe3                                  ..
    decimal
              0  227
    datetime (2014-01-12T10:03:52)
    0000   0x34 0x43 0x0a 0x0c 0x1e                   4C...
    body (0)
    HOUR BITS: [0, 1, 0] YEAR BITS: [0, 0, 0, 1]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x00 0xec 0x08 0x0d 0x0a 0x0c 0x1f 0x00    ........
    0008   0xcd 0x23 0x0d 0x0a 0x0c 0x0a 0x9d 0xcd    .#......
    0010   0x28 0x2d 0x0a 0x0c 0x5b 0x9d 0xd5 0x28    (-..[..(
    0018   0x0d 0x0a 0x0c 0x00 0x50 0x0d 0x2d         ....P.-
##### DEBUG DECIMAL
              0  236    8   13   10   12   31    0
            205   35   13   10   12   10  157  205
             40   45   10   12   91  157  213   40
             13   10   12    0   80   13   45
XXX:???:XXX 2010-03-13T08:44:00
`end logs/ReadHistoryData-page-12.data: 2 records`

### analysis/bewest-pump/ReadHistoryData-page-13.data.list_opcodes.markdown
WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-13.data
#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x5c 0x08 0xb0 0x82 0x14 0x84 0xd2 0x14    \.......
    0008   0x01 0x24 0x24 0x00 0xee 0x0a 0x53 0x06    .$$...S.
    0010   0x0c 0x07 0x00 0x00 0x05 0x3c 0xc6 0x0c    .....<..
    0018   0x6d 0xc6 0x0c 0x05 0x10 0xa9 0x60 0x12    m.....`.
    0020   0x05 0x00 0x00 0x05 0x3c 0x03              ....<.
##### DEBUG DECIMAL
             92    8  176  130   20  132  210   20
              1   36   36    0  238   10   83    6
             12    7    0    0    5   60  198   12
            109  198   12    5   16  169   96   18
              5    0    0    5   60    3
XXX:???:XXX 2004-04-02T16:08:28
`end logs/ReadHistoryData-page-13.data: 0 records`

### analysis/bewest-pump/ReadHistoryData-page-14.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-15.data.list_opcodes.markdown
              5    0  118   95  141    3    0    0
              4  172    3   88   72    1   84   28
              0  116    1   84   28    1   84  100
              0    0    0    0    0    0    3    3
              0    0    0   12    0  232    0    0
              0
    HOUR BITS: [1, 0, 0] DAY BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 30 CalForBG 2012-12-01T21:31:52 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x72                                  .r
    decimal
             10  114
    datetime (2012-12-01T21:31:52)
    0000   0xf4 0x1f 0x35 0x01 0x0c                   ..5..
    body (0)
    

#### RECORD 31 BolusWizard 2012-12-01T21:32:04 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x72                                  [r
    decimal
             91  114
    datetime (2012-12-01T21:32:04)
    0000   0xc4 0x20 0x15 0x01 0x0c                   . ...
    body (22)
    hex
    0000   0x47 0x50 0x0d 0x2d 0x6a 0x00 0x36 0x00    GP.-j.6.
    0008   0x00 0x00 0x00 0x36 0x7d 0x1e 0x00 0xdd    ...6}...
    0010   0x20 0x15 0x01 0x0c 0x01 0x36               ....6
    decimal
             71   80   13   45  106    0   54    0
              0    0    0   54  125   30    0  221
             32   21    1   12    1   54
    HOUR BITS: [0, 0, 1]

#### RECORD 32 ResultTotals MIDNIGHT!?: (2015, 0, 0, 31, 12, 1) head[5], body[41] 0x07
    op hex (5)
    0000   0x07 0x00 0xc4 0x20 0x55                   ... U
    decimal
              7    0  196   32   85
    datetime (MIDNIGHT!?: (2015, 0, 0, 31, 12, 1))
    0000   0x01 0x0c 0x1f 0x00 0xdf                   .....
    body (41)
    hex
    0000   0x20 0x15 0x01 0x0c 0x0a 0x72 0xe8 0x20     ....r. 
    0008   0x35 0x01 0x0c 0x5b 0x72 0xfa 0x21 0x15    5..[r.!.
    0010   0x01 0x0c 0x64 0x50 0x0d 0x2d 0x6a 0x00    ..dP.-j.
    0018   0x4c 0x00 0x00 0x07 0x00 0x4c 0x7d 0x5c    L....L}\
    0020   0x05 0x1a 0x09 0x04 0x01 0x2b 0x2b 0x00    .....++.
    0028   0xfa                                       .
    decimal
             32   21    1   12   10  114  232   32
             53    1   12   91  114  250   33   21
              1   12  100   80   13   45  106    0
             76    0    0    7    0   76  125   92
              5   26    9    4    1   43   43    0
            250
    YEAR BITS: [1, 1, 0, 1]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x21 0x95 0x01 0x0c 0x07 0x00 0x00 0x04    !.......
    0008   0xd8 0xc1 0x0c 0x6d 0xc1 0x0c 0x05 0x00    ...m....
    0010   0x72 0x72 0x72 0x02 0x00 0x00 0x04 0xd8    rrr.....
    0018   0x03 0x84 0x49 0x01 0x54 0x1b 0x00         ..I.T..
##### DEBUG DECIMAL
             33  149    1   12    7    0    0    4
            216  193   12  109  193   12    5    0
            114  114  114    2    0    0    4  216
              3  132   73    1   84   27    0
XXX:???:XXX 2007-02-12T01:21:33
`end logs/ReadHistoryData-page-15.data: 33 records`

### analysis/bewest-pump/ReadHistoryData-page-16.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-17.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-18.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-19.data.list_opcodes.markdown
WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-19.data
should eat up to null
found 4 extra
#### RECORD 0 BolusWizard 2012-11-12T00:55:42 head[2], body[26] 0x5b
    op hex (2)
    0000   0x5b 0x7e                                  [~
    decimal
             91  126
    datetime (2012-11-12T00:55:42)
    0000   0xaa 0xf7 0x00 0x0c 0x0c                   .....
    body (26)
    hex
    0000   0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00    .P.-j...
    0008   0x00 0x07 0x00 0x0b 0x7d 0x5c 0x08 0x58    ....}\.X
    0010   0x97 0x04 0x30 0x05 0x14 0x34 0xc8 0x91    ..0..4..
    0018   0xf8 0x00                                  ..
    decimal
             15   80   13   45  106    0   11    0
              0    7    0   11  125   92    8   88
            151    4   48    5   20   52  200  145
            248    0
    HOUR BITS: [1, 1, 1]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x00 0xaa 0xf7 0x40 0x0c 0x0c 0x0a 0x0c    ...@....
    0008   0x8b 0xc3 0x28 0x0c 0x8c 0x5b 0x0c 0x8d    ..(..[..
    0010   0xc3 0x08 0x0c 0x0c 0x00 0x51 0x0d 0x2d    .....Q.-
    0018   0x6a 0x1f 0x00 0x00 0x00 0x00 0x00         j......
##### DEBUG DECIMAL
              0  170  247   64   12   12   10   12
            139  195   40   12  140   91   12  141
            195    8   12   12    0   81   13   45
            106   31    0    0    0    0    0
XXX:???:XXX
Traceback (most recent call last):
  File "list_opcodes.py", line 334, in <module>
    main( )
  File "list_opcodes.py", line 318, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 262, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 590, in parse_date
    raise NotADate(e)
pump.history.NotADate: day is out of range for month

### analysis/bewest-pump/ReadHistoryData-page-1.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-20.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-21.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-22.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-23.data.list_opcodes.markdown
WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-23.data
#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x5c 0x14 0x0c 0x69 0x04 0x20 0xd7 0x04    \..i. ..
    0008   0x14 0xe1 0x04 0x3c 0x77 0x14 0x6c 0x81    ...<w.l.
    0010   0x14 0x4c 0xa9 0x14 0x01 0x2d 0x2d 0x00    .L...--.
    0018   0xa6 0xbb 0x52 0x1d 0x0c 0x0a 0x78 0xad    ..R...x.
    0020   0xab 0x33 0x1d 0x0c 0x07 0x00              .3....
##### DEBUG DECIMAL
             92   20   12  105    4   32  215    4
             20  225    4   60  119   20  108  129
             20   76  169   20    1   45   45    0
            166  187   82   29   12   10  120  173
            171   51   29   12    7    0
XXX:???:XXX 2004-04-09T12:20:28
`end logs/ReadHistoryData-page-23.data: 0 records`

### analysis/bewest-pump/ReadHistoryData-page-24.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-25.data.list_opcodes.markdown
    0008   0x00 0x08 0x00 0x10 0x7d 0x5c 0x05 0xbc    ....}\..
    0010   0xbb 0x04 0x01 0x14 0x14 0x00              ......
    decimal
              0   80   13   45  106   24    0    0
              0    8    0   16  125   92    5  188
            187    4    1   20   20    0
    HOUR BITS: [1, 0, 1]

#### RECORD 59 CalForBG 2012-10-26T16:11:18 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-10-26T16:11:18)
    0000   0x92 0x8b 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 60 CalForBG 2012-10-26T16:14:35 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-10-26T16:14:35)
    0000   0xa3 0x8e 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 61 CalForBG 2012-10-26T16:15:40 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-10-26T16:15:40)
    0000   0xa8 0x8f 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

should eat up to null
found 3 extra
#### RECORD 62 BolusWizard 2012-10-26T16:15:54 head[2], body[25] 0x5b
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2012-10-26T16:15:54)
    0000   0xb6 0x8f 0x10 0x1a 0x0c                   .....
    body (25)
    hex
    0000   0x1a 0x50 0x0d 0x2d 0x6a 0xfd 0x14 0xf0    .P.-j...
    0008   0x00 0x02 0x00 0x11 0x7d 0x5c 0x08 0x50    ....}\.P
    0010   0xdd 0x04 0xbc 0x91 0x14 0x01 0x11 0x11    ........
    0018   0x00                                       .
    decimal
             26   80   13   45  106  253   20  240
              0    2    0   17  125   92    8   80
            221    4  188  145   20    1   17   17
              0
    HOUR BITS: [1, 0, 0]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x00 0x00 0x00 0x00 0x00 0x38 0xa2         .....8.
##### DEBUG DECIMAL
              0    0    0    0    0   56  162
XXX:???:XXX
Traceback (most recent call last):
  File "list_opcodes.py", line 334, in <module>
    main( )
  File "list_opcodes.py", line 318, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 262, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 590, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-26.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-27.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-28.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-29.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-2.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-30.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-31.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-32.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-33.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-34.data.list_opcodes.markdown
    0000   0x9e 0x75 0x2d 0x14 0x0c                   .u-..
    body (0)
    HOUR BITS: [0, 1, 1]

should eat up to null
found 12 extra
#### RECORD 45 BolusWizard 2012-09-20T13:53:58 head[2], body[34] 0x5b
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2012-09-20T13:53:58)
    0000   0xba 0x75 0x0d 0x14 0x0c                   .u...
    body (34)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x18 0x00 0x07 0x7d 0x5c 0x11 0x4c    ....}\.L
    0010   0x09 0x04 0x08 0x3b 0x04 0x16 0x77 0x04    ...;..w.
    0018   0x26 0x2b 0x14 0x66 0x35 0x14 0x01 0x07    &+.f5...
    0020   0x07 0x00                                  ..
    decimal
             10   80   13   45  106    0    7    0
              0   24    0    7  125   92   17   76
              9    4    8   59    4   22  119    4
             38   43   20  102   53   20    1    7
              7    0
    HOUR BITS: [0, 1, 1]

#### RECORD 46 CalForBG 2012-09-20T18:37:12 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-09-20T18:37:12)
    0000   0x8c 0x65 0x32 0x14 0x0c                   .e2..
    body (0)
    HOUR BITS: [0, 1, 1]

should eat up to null
found 9 extra
#### RECORD 47 BolusWizard 2012-09-20T19:02:06 head[2], body[31] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-20T19:02:06)
    0000   0x86 0x42 0x13 0x14 0x0c                   .B...
    body (31)
    hex
    0000   0x29 0x50 0x0d 0x2d 0x6a 0x00 0x1f 0x00    )P.-j...
    0008   0x00 0x00 0x00 0x1f 0x7d 0x5c 0x0e 0x1a    ....}\..
    0010   0x34 0x14 0x4e 0x3e 0x14 0x08 0x70 0x14    4.N>..p.
    0018   0x16 0xac 0x14 0x01 0x1f 0x1f 0x00         .......
    decimal
             41   80   13   45  106    0   31    0
              0    0    0   31  125   92   14   26
             52   20   78   62   20    8  112   20
             22  172   20    1   31   31    0
    HOUR BITS: [0, 1, 0]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x00 0x00 0x00 0x00 0x00 0x00 0x1f 0xf2    ........
##### DEBUG DECIMAL
              0    0    0    0    0    0   31  242
XXX:???:XXX
Traceback (most recent call last):
  File "list_opcodes.py", line 334, in <module>
    main( )
  File "list_opcodes.py", line 318, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 262, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 590, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-35.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-3.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-4.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-5.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-6.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-7.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-8.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-9.data.list_opcodes.markdown

