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
  File "list_opcodes.py", line 329, in <module>
    main( )
  File "list_opcodes.py", line 313, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 257, in find_dates
