## START logs/ReadHistoryData-page-43.data
Traceback (most recent call last):
  File "list_history.py", line 99, in <module>
    main( )
  File "list_history.py", line 83, in main
    records = find_records(stream)
  File "list_history.py", line 67, in find_records
    record = parse_record( stream, B )
  File "/home/bewest/src/decoding-carelink/decocare/history.py", line 190, in parse_record
    record.parse( head + date + body )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 59, in parse
    return self.decode( )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 112, in decode
    self.parse_time( )
  File "/home/bewest/src/decoding-carelink/decocare/records/base.py", line 109, in parse_time
    self.datetime = parse_date(self.date)
  File "/home/bewest/src/decoding-carelink/decocare/records/times.py", line 241, in parse_date
    return parse_date_strict(date)
  File "/home/bewest/src/decoding-carelink/decocare/records/times.py", line 261, in parse_date_strict
    (year, month, day, hours, minutes, seconds) = unmask_date(data)
  File "/home/bewest/src/decoding-carelink/decocare/records/times.py", line 226, in unmask_date
    seconds = parse_seconds(data[0])
IndexError: bytearray index out of range
