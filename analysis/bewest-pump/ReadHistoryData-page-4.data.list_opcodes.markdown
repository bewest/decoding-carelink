WARNING: No route found for IPv6 destination :: (no default route?)
## START logs/ReadHistoryData-page-4.data
found 0 nulls
Traceback (most recent call last):
  File "list_opcodes.py", line 358, in <module>
    main( )
  File "list_opcodes.py", line 342, in main
    records = find_dates(stream)
  File "list_opcodes.py", line 273, in find_dates
    records[-1].body.extend(nulls)
IndexError: list index out of range
