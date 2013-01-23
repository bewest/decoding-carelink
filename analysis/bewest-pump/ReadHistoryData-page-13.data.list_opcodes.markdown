WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-13.data
Traceback (most recent call last):
  File "list_opcodes.py", line 317, in <module>
    main( )
  File "list_opcodes.py", line 301, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 247, in find_dates
    assert datetime is not None, "\n%s" % lib.hexdump(bolus)
AssertionError: 
0000   0x5c 0x08 0xb0 0x82 0x14 0x84 0xd2 0x14    \.......
0008   0x01 0x24 0x24 0x00 0xee 0x0a              .$$...
