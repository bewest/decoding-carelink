WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-23.data
Traceback (most recent call last):
  File "list_opcodes.py", line 317, in <module>
    main( )
  File "list_opcodes.py", line 301, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 247, in find_dates
    assert datetime is not None, "\n%s" % lib.hexdump(bolus)
AssertionError: 
0000   0x5c 0x14 0x0c 0x69 0x04 0x20 0xd7 0x04    \..i. ..
0008   0x14 0xe1 0x04 0x3c 0x77 0x14              ...<w.
