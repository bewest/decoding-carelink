## START logs/ReadHistoryData-page-20.data
Traceback (most recent call last):
  File "list_history.py", line 99, in <module>
    main( )
  File "list_history.py", line 83, in main
    records = find_records(stream)
  File "list_history.py", line 67, in find_records
    record = parse_record( stream, B )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 689, in parse_record
    record.parse( head + date + body )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 330, in parse
    return self.decode( )
  File "/home/bewest/src/decoding-carelink/pump/history.py", line 576, in decode
    correction = ( twos_comp( self.body[7], 8 )
IndexError: bytearray index out of range
