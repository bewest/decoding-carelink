## START logs/ReadHistoryData-page-4.data
Traceback (most recent call last):
  File "list_history.py", line 105, in <module>
    main( )
  File "list_history.py", line 89, in main
    records = find_records(stream, opts)
  File "list_history.py", line 73, in find_records
    record = parse_record( stream, B, larger=opts.larger )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 265, in parse_record
    record.parse( head + date + body )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 63, in parse
    return self.decode( )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 119, in decode
    self.parse_time( )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 191, in parse_time
    self.datetime = date = datetime(*mid)
ValueError: day is out of range for month
