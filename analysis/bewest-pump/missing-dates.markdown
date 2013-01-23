### analysis/bewest-pump/ReadHistoryData-page-0.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-10.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-11.data.list_opcodes.markdown
             91    0
    datetime (2012-12-15T20:59:43)
    0000   0xeb 0x3b 0x14 0x0f 0x0c                   .;...
    body (22)
    hex
    0000   0x0a 0x50 0x0d 0x2d 0x6a 0x00 0x07 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x07 0x7d 0x5c 0x05 0x5c    ....}\.\
    0010   0x37 0x04 0x01 0x07 0x07 0x00              7.....
    decimal
             10   80   13   45  106    0    7    0
              0    0    0    7  125   92    5   92
             55    4    1    7    7    0
    HOUR BITS: [0, 0, 1]

should eat up to null
found 3 extra
#### RECORD 24 BolusWizard 2012-12-15T21:37:07 head[2], body[25] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-12-15T21:37:07)
    0000   0xc7 0x25 0x15 0x0f 0x0c                   .%...
    body (25)
    hex
    0000   0x0b 0x50 0x0d 0x2d 0x6a 0x00 0x08 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x08 0x7d 0x5c 0x08 0x1c    ....}\..
    0010   0x2b 0x04 0x5c 0x5d 0x04 0x01 0x08 0x08    +.\]....
    0018   0x00                                       .
    decimal
             11   80   13   45  106    0    8    0
              0    0    0    8  125   92    8   28
             43    4   92   93    4    1    8    8
              0
    HOUR BITS: [0, 0, 1]

#### RECORD 25 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x04 0x08 0xcf 0x0c                   .....
    body (44)
    hex
    0000   0x6d 0xcf 0x0c 0x05 0x00 0x7b 0x7b 0x7b    m....{{{
    0008   0x01 0x00 0x00 0x04 0x08 0x03 0x70 0x55    ......pU
    0010   0x00 0x98 0x0f 0x00 0x33 0x00 0x98 0x0f    ....3...
    0018   0x00 0x98 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x03 0x03 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109  207   12    5    0  123  123  123
              1    0    0    4    8    3  112   85
              0  152   15    0   51    0  152   15
              0  152  100    0    0    0    0    0
              0    3    3    0    0    0   12    0
            232    0    0    0
    

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x1e 0x00 0xd5 0x2f 0x09 0x10 0x0c 0x1f    .../....
    0008   0x00 0xdd 0x04 0x0a 0x10 0x0c 0x0a 0x8f    ........
    0010   0xf9 0x39 0x2a 0x10 0x0c 0x5b 0x8f 0xfb    .9*..[..
    0018   0x3a 0x0a 0x10 0x0c 0x39 0x50 0x0d         :...9P.
##### DEBUG DECIMAL
             30    0  213   47    9   16   12   31
              0  221    4   10   16   12   10  143
            249   57   42   16   12   91  143  251
             58   10   16   12   57   80   13
XXX:???:XXX
Traceback (most recent call last):
  File "list_opcodes.py", line 327, in <module>
    main( )
  File "list_opcodes.py", line 311, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 255, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 268, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-12.data.list_opcodes.markdown
WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-12.data
#### RECORD 0 Record 2010-12-10T01:20:30 head[9], body[0] 0x5c
    op hex (9)
    0000   0x5c 0x0b 0x14 0x08 0x04 0x06 0xd4 0x14    \.......
    0008   0x92                                       .
    decimal
             92   11   20    8    4    6  212   20
            146
    datetime (2010-12-10T01:20:30)
    0000   0xde 0x14 0x01 0x3a 0x3a                   ...::
    body (0)
    YEAR BITS: [0, 0, 1, 1]

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
            109  190  140    5    0  118   95  141
              3    0    0    4  172    3   88   72
              1   84   28    0  116    1   84   28
              1   84  100    0    0    0    0    0
              0    3    3    0    0    0   12    0
            232    0    0    0
    YEAR BITS: [1, 0, 0, 0]

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

#### RECORD 32 ResultTotals 2012-12-01T21:32:04 head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (2012-12-01T21:32:04)
    0000   0xc4 0x20 0x55 0x01 0x0c                   . U..
    body (44)
    hex
    0000   0x1f 0x00 0xdf 0x20 0x15 0x01 0x0c 0x0a    ... ....
    0008   0x72 0xe8 0x20 0x35 0x01 0x0c 0x5b 0x72    r. 5..[r
    0010   0xfa 0x21 0x15 0x01 0x0c 0x64 0x50 0x0d    .!...dP.
    0018   0x2d 0x6a 0x00 0x4c 0x00 0x00 0x07 0x00    -j.L....
    0020   0x4c 0x7d 0x5c 0x05 0x1a 0x09 0x04 0x01    L}\.....
    0028   0x2b 0x2b 0x00 0xfa                        ++..
    decimal
             31    0  223   32   21    1   12   10
            114  232   32   53    1   12   91  114
            250   33   21    1   12  100   80   13
             45  106    0   76    0    0    7    0
             76  125   92    5   26    9    4    1
             43   43    0  250
    HOUR BITS: [0, 0, 1]

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
              0    0    0   23  125   92   17  132
             11    4    4   21    4  100   95   20
             28  165   20  140  205   20    1   10
             10    0
    HOUR BITS: [1, 1, 1]

#### RECORD 2 Bolus 2012-11-15T19:56:29 head[4], body[0] 0x01
    op hex (4)
    0000   0x01 0x0d 0x0d 0x01                        ....
    decimal
              1   13   13    1
    datetime (2012-11-15T19:56:29)
    0000   0x9d 0xf8 0xb3 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 1, 1]

#### RECORD 3 CalForBG 2012-11-15T21:02:01 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x79                                  .y
    decimal
             10  121
    datetime (2012-11-15T21:02:01)
    0000   0x81 0xc2 0x35 0x0f 0x0c                   ..5..
    body (0)
    HOUR BITS: [1, 1, 0]

#### RECORD 4 CalForBG 2012-11-15T23:07:56 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x4a                                  .J
    decimal
             10   74
    datetime (2012-11-15T23:07:56)
    0000   0xb8 0xc7 0x37 0x0f 0x0c                   ..7..
    body (0)
    HOUR BITS: [1, 1, 0]

#### RECORD 5 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x05 0x68 0xaf 0x8c                   ..h..
    body (44)
    hex
    0000   0x6d 0xaf 0x8c 0x05 0x00 0x5d 0x4a 0x79    m....]Jy
    0008   0x05 0x00 0x00 0x05 0x68 0x03 0x78 0x40    ....h.x@
    0010   0x01 0xf0 0x24 0x00 0xb4 0x01 0xf0 0x24    ..$....$
    0018   0x01 0xf0 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x05 0x05 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109  175  140    5    0   93   74  121
              5    0    0    5  104    3  120   64
              1  240   36    0  180    1  240   36
              1  240  100    0    0    0    0    0
              0    5    5    0    0    0   12    0
            232    0    0    0
    YEAR BITS: [1, 0, 0, 0]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x34 0xc8 0xa6 0xeb 0x0b 0x10 0x0c 0x1e    4.......
    0008   0x00 0x93 0xd4 0x0e 0x10 0x0c 0x1f 0x00    ........
    0010   0x95 0xe8 0x0e 0x10 0x0c 0x0a 0x60 0x80    ......`.
    0018   0xcf 0x30 0x10 0x0c 0x5b 0x60 0xa3         .0..[`.
##### DEBUG DECIMAL
             52  200  166  235   11   16   12   30
              0  147  212   14   16   12   31    0
            149  232   14   16   12   10   96  128
            207   48   16   12   91   96  163
XXX:???:XXX 2011-03-11T06:08:52
`end logs/ReadHistoryData-page-18.data: 6 records`

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
  File "list_opcodes.py", line 327, in <module>
    main( )
  File "list_opcodes.py", line 311, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 255, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 268, in parse_date
    raise NotADate(e)
pump.history.NotADate: day is out of range for month

### analysis/bewest-pump/ReadHistoryData-page-1.data.list_opcodes.markdown
            141    4  142  151    4    1    3    3
              0
    HOUR BITS: [0, 1, 0]

#### RECORD 16 CalForBG 2013-01-15T18:45:59 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xcb                                  ..
    decimal
             10  203
    datetime (2013-01-15T18:45:59)
    0000   0x3b 0x6d 0x32 0x0f 0x0d                   ;m2..
    body (0)
    HOUR BITS: [0, 1, 1]

should eat up to null
found 6 extra
#### RECORD 17 BolusWizard 2013-01-15T18:46:17 head[2], body[28] 0x5b
    op hex (2)
    0000   0x5b 0xcb                                  [.
    decimal
             91  203
    datetime (2013-01-15T18:46:17)
    0000   0x11 0x6e 0x12 0x0f 0x0d                   .n...
    body (28)
    hex
    0000   0x37 0x50 0x0d 0x2d 0x6a 0x11 0x2a 0x00    7P.-j.*.
    0008   0x00 0x14 0x00 0x2a 0x7d 0x5c 0x0b 0x0c    ...*}\..
    0010   0x16 0x04 0x9e 0xa2 0x04 0x8e 0xac 0x04    ........
    0018   0x01 0x2a 0x2a 0x00                        .**.
    decimal
             55   80   13   45  106   17   42    0
              0   20    0   42  125   92   11   12
             22    4  158  162    4  142  172    4
              1   42   42    0
    HOUR BITS: [0, 1, 1]

#### RECORD 18 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x05 0x56 0x0f 0x8d                   ..V..
    body (44)
    hex
    0000   0x6d 0x0f 0x8d 0x05 0x00 0x9b 0x4c 0xeb    m.....L.
    0008   0x06 0x00 0x00 0x05 0x56 0x03 0x76 0x41    ....V.vA
    0010   0x01 0xe0 0x23 0x00 0xa0 0x01 0xe0 0x23    ..#....#
    0018   0x01 0xd4 0x61 0x00 0x0c 0x03 0x00 0x00    ..a.....
    0020   0x00 0x04 0x03 0x01 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109   15  141    5    0  155   76  235
              6    0    0    5   86    3  118   65
              1  224   35    0  160    1  224   35
              1  212   97    0   12    3    0    0
              0    4    3    1    0    0   12    0
            232    0    0    0
    YEAR BITS: [1, 0, 0, 0]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x0a 0xf5 0x00 0x53 0x26 0x10 0x0d 0x5b    ...S&..[
    0008   0xf5 0x02 0x53 0x06 0x10 0x0d 0x00 0x50    ..S....P
    0010   0x0d 0x2d 0x6a 0x1a 0x00 0x00 0x00 0x00    .-j.....
    0018   0x00 0x1a 0x7d 0x01 0x1a 0x1a 0x00         ..}....
##### DEBUG DECIMAL
             10  245    0   83   38   16   13   91
            245    2   83    6   16   13    0   80
             13   45  106   26    0    0    0    0
              0   26  125    1   26   26    0
XXX:???:XXX 2006-03-03T00:53:10
`end logs/ReadHistoryData-page-1.data: 19 records`

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

#### RECORD 59 CalForBG 2012-10-10T16:11:18 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x46                                  .F
    decimal
             10   70
    datetime (2012-10-10T16:11:18)
    0000   0x92 0x8b 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 60 CalForBG 2012-10-10T16:14:35 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x50                                  .P
    decimal
             10   80
    datetime (2012-10-10T16:14:35)
    0000   0xa3 0x8e 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 61 CalForBG 2012-10-10T16:15:40 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x5c                                  .\
    decimal
             10   92
    datetime (2012-10-10T16:15:40)
    0000   0xa8 0x8f 0x30 0x1a 0x0c                   ..0..
    body (0)
    HOUR BITS: [1, 0, 0]

should eat up to null
found 3 extra
#### RECORD 62 BolusWizard 2012-10-10T16:15:54 head[2], body[25] 0x5b
    op hex (2)
    0000   0x5b 0x5c                                  [\
    decimal
             91   92
    datetime (2012-10-10T16:15:54)
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
  File "list_opcodes.py", line 327, in <module>
    main( )
  File "list_opcodes.py", line 311, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 255, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 268, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-26.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-27.data.list_opcodes.markdown
    hex
    0000   0x00                                       .
    decimal
              0
    HOUR BITS: [1, 0, 0]

#### RECORD 16 TempBasal[eof] 2012-10-15T21:14:43 head[2], body[0] 0x16
    op hex (2)
    0000   0x16 0x04                                  ..
    decimal
             22    4
    datetime (2012-10-15T21:14:43)
    0000   0xab 0x8e 0x15 0x0f 0x0c                   .....
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 17 CalForBG 2012-10-15T21:33:41 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x08                                  ..
    decimal
             10    8
    datetime (2012-10-15T21:33:41)
    0000   0xa9 0xa1 0x35 0x0f 0x8c                   ..5..
    body (0)
    HOUR BITS: [1, 0, 1] YEAR BITS: [1, 0, 0, 0]

#### RECORD 18 CalForBG 2012-10-15T22:12:34 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0xe3                                  ..
    decimal
             10  227
    datetime (2012-10-15T22:12:34)
    0000   0xa2 0x8c 0x36 0x0f 0x0c                   ..6..
    body (0)
    HOUR BITS: [1, 0, 0]

#### RECORD 19 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x07 0xa0 0xaf 0x0c                   .....
    body (44)
    hex
    0000   0x6d 0xaf 0x0c 0x05 0x11 0x33 0x9a 0xbc    m....3..
    0008   0x0d 0x00 0x00 0x07 0xa0 0x03 0xa0 0x30    .......0
    0010   0x04 0x00 0x34 0x00 0x8a 0x04 0x00 0x34    ..4....4
    0018   0x01 0xa0 0x29 0x02 0x60 0x3b 0x00 0x00    ..).`;..
    0020   0x00 0x08 0x03 0x04 0x01 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109  175   12    5   17   51  154  188
             13    0    0    7  160    3  160   48
              4    0   52    0  138    4    0   52
              1  160   41    2   96   59    0    0
              0    8    3    4    1    0   12    0
            232    0    0    0
    

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x0a 0x4d 0x97 0x8c 0x21 0x10 0x0c 0x5b    .M..!..[
    0008   0x00 0xa7 0x8a 0x0e 0x10 0x0c 0x09 0x50    .......P
    0010   0x0d 0x2d 0x6a 0x00 0x06 0x00 0x00 0x00    .-j.....
    0018   0x00 0x06 0x7d 0x01 0x06 0x06 0x00         ..}....
##### DEBUG DECIMAL
             10   77  151  140   33   16   12   91
              0  167  138   14   16   12    9   80
             13   45  106    0    6    0    0    0
              0    6  125    1    6    6    0
XXX:???:XXX 2001-01-12T23:13:10
`end logs/ReadHistoryData-page-27.data: 20 records`

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
#### RECORD 45 BolusWizard 2012-09-04T13:53:58 head[2], body[34] 0x5b
    op hex (2)
    0000   0x5b 0x73                                  [s
    decimal
             91  115
    datetime (2012-09-04T13:53:58)
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

#### RECORD 46 CalForBG 2012-09-04T18:37:12 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x43                                  .C
    decimal
             10   67
    datetime (2012-09-04T18:37:12)
    0000   0x8c 0x65 0x32 0x14 0x0c                   .e2..
    body (0)
    HOUR BITS: [0, 1, 1]

should eat up to null
found 9 extra
#### RECORD 47 BolusWizard 2012-09-04T19:02:06 head[2], body[31] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-04T19:02:06)
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
  File "list_opcodes.py", line 327, in <module>
    main( )
  File "list_opcodes.py", line 311, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 255, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 268, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-35.data.list_opcodes.markdown
    decimal
             10  128
    datetime (2012-09-15T16:54:31)
    0000   0x9f 0x76 0x30 0x0f 0x0c                   .v0..
    body (0)
    HOUR BITS: [0, 1, 1]

should eat up to null
#### RECORD 28 BolusWizard 2012-09-15T19:13:59 head[2], body[22] 0x5b
    op hex (2)
    0000   0x5b 0x00                                  [.
    decimal
             91    0
    datetime (2012-09-15T19:13:59)
    0000   0xbb 0x4d 0x13 0x0f 0x0c                   .M...
    body (22)
    hex
    0000   0x1e 0x50 0x0d 0x2d 0x6a 0x00 0x17 0x00    .P.-j...
    0008   0x00 0x00 0x00 0x17 0x7d 0x5c 0x05 0xb4    ....}\..
    0010   0x35 0x14 0x01 0x17 0x17 0x00              5.....
    decimal
             30   80   13   45  106    0   23    0
              0    0    0   23  125   92    5  180
             53   20    1   23   23    0
    HOUR BITS: [0, 1, 0]

#### RECORD 29 CalForBG 2012-09-15T20:44:41 head[2], body[0] 0x0a
    op hex (2)
    0000   0x0a 0x42                                  .B
    decimal
             10   66
    datetime (2012-09-15T20:44:41)
    0000   0xa9 0x6c 0x34 0x0f 0x0c                   .l4..
    body (0)
    HOUR BITS: [0, 1, 1]

#### RECORD 30 ResultTotals MIDNIGHT!? head[2], body[44] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x04 0x66 0x8f 0x8c                   ..f..
    body (44)
    hex
    0000   0x6d 0x8f 0x8c 0x05 0x00 0x80 0x42 0xf2    m.....B.
    0008   0x05 0x00 0x00 0x04 0x66 0x03 0x56 0x4c    ....f.VL
    0010   0x01 0x10 0x18 0x00 0x5b 0x01 0x10 0x18    ....[...
    0018   0x01 0x10 0x64 0x00 0x00 0x00 0x00 0x00    ..d.....
    0020   0x00 0x02 0x02 0x00 0x00 0x00 0x0c 0x00    ........
    0028   0xe8 0x00 0x00 0x00                        ....
    decimal
            109  143  140    5    0  128   66  242
              5    0    0    4  102    3   86   76
              1   16   24    0   91    1   16   24
              1   16  100    0    0    0    0    0
              0    2    2    0    0    0   12    0
            232    0    0    0
    YEAR BITS: [1, 0, 0, 0]

#### MISSING DATETIME, reading more to debug
##### DEBUG HEX
    0000   0x1e 0x00 0xbb 0x4c 0x08 0x10 0x0c 0x1f    ...L....
    0008   0x00 0xba 0x60 0x08 0x10 0x0c 0x0a 0xaa    ..`.....
    0010   0xab 0x60 0x2a 0x10 0x0c 0x5b 0xaa 0xaf    .`*..[..
    0018   0x60 0x0a 0x10 0x0c 0x00 0x50 0x0d         `....P.
##### DEBUG DECIMAL
             30    0  187   76    8   16   12   31
              0  186   96    8   16   12   10  170
            171   96   42   16   12   91  170  175
             96   10   16   12    0   80   13
XXX:???:XXX
Traceback (most recent call last):
  File "list_opcodes.py", line 327, in <module>
    main( )
  File "list_opcodes.py", line 311, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 255, in find_dates
    print "XXX:???:XXX", history.parse_date(bolus).isoformat( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 268, in parse_date
    raise NotADate(e)
pump.history.NotADate: month must be in 1..12

### analysis/bewest-pump/ReadHistoryData-page-3.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-4.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-5.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-6.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-7.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-8.data.list_opcodes.markdown

### analysis/bewest-pump/ReadHistoryData-page-9.data.list_opcodes.markdown

