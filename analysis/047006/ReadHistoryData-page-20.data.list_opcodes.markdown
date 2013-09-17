## START logs/ReadHistoryData-page-20.data
Traceback (most recent call last):
  File "list_history.py", line 105, in <module>
    main( )
  File "list_history.py", line 89, in main
    records = find_records(stream, opts)
  File "list_history.py", line 73, in find_records
    record = parse_record( stream, B, larger=opts.larger )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 226, in parse_record
    record.parse( head + date + body )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 63, in parse
    return self.decode( )
  File "/home/bewest/src/decoding-carelink/decocare/records/bolus.py", line 82, in decode
    correction = ( twos_comp( self.body[7], 8 )
IndexError: bytearray index out of range
