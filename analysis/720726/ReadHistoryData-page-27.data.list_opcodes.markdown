## START logs/ReadHistoryData-page-27.data
Traceback (most recent call last):
  File "list_history.py", line 99, in <module>
    main( )
  File "list_history.py", line 83, in main
    records = find_records(stream)
  File "list_history.py", line 67, in find_records
    record = parse_record( stream, B )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 738, in parse_record
    record.parse( head + date + body )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 366, in parse
    return self.decode( )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 684, in decode
    doses.append( decode_unabsorbed(*head) )
TypeError: decode_unabsorbed() takes at least 3 arguments (1 given)
