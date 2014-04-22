
from datetime import *
"""def str_to_int(string):
  return

def int_to_hex():

def int_to_hexstr():
  # convert integer to string
  return '{0:02x}'.format(op_code)

def hex_to_int():
  # convert hex char(s) to int
  '{0:08b}'.format()
"""


# -*- coding: utf-8 *-*
class op_code_stats:
#  op_code = 0
#  op_code_str = '{0:02x}'.format(op_code)
#  num_records = 0
#  record_lens = Counter()

  def __init__(self, op_code, data):
    self.op_code = op_code
    self.op_code_str = '{0:02x}'.format(op_code)
    records = data.split(self.op_code_str)
    self.num_records = len(records)
    from collections import Counter
    self.record_lens = Counter()
    for record in records:
      record_len = len(record)
      if record_len > 1 and record_len < 500:
        self.record_lens[str(record_len)] += 1

  def is_likely_op(self):
    if self.num_records < 5:
      return False
    most_common = self.record_lens.most_common(1)
    if not most_common:
      return False
    if int(most_common[0][0]) < 5 or int(most_common[0][0]) > 20:
      return False
    if most_common[0][1] * 4 < self.num_records:
      return False
    return True

  def str(self):
    string = "Data "+self.op_code_str+" ("+str(self.num_records)+"):  "
    most_common = self.record_lens.most_common(7)
    for record_size in most_common:
      string += str(record_size[0]) +" ("+ str(record_size[1]) + ")\t"
    return string
    #for record in self.record_lens:
    #  string += record+"["+self.record_lens[record]+"]\t"


class record():

  def __init__(self, op_code, raw):
    self.is_valid_record = True
    self.op_code = op_code
    self.raw = raw
    self.hex_bytes = array.array('B', raw.decode("hex"))
    self.binary = bin(int(raw, 16))[2:].zfill(56)
    # parse_date seems to not be quite correct
#    self.bwdatetime = parse_date(self.hex_bytes[-5:])
#    print str(self.bwdatetime)
    self.mydatetime = self.mydate(raw)


  def mydate(self, raw):
    year = int(self.binary[-8:], 2)
    # month
    month = int(self.binary[-24:-22]+self.binary[-16:-14], 2)
#    day_offset possibilities: -24, -57 - doesn't seem quite right
    day_offset = -24
    # if day is split possibilities (size 2):
    day = int(self.binary[day_offset:day_offset+5], 2)
    # hour offset options: -21 -33 -38 => -21 looks almost perfect
    hour_offset = -21
    hour = int(self.binary[hour_offset:hour_offset+5], 2)
#    hour = int(self.binary[-21:-17], 2)
    # minute offset options: -27 -28 => -28 looks to be the best but not perfect
    min_offset = -28
    minute = int(self.binary[min_offset:min_offset+6], 2)
#    print_offset = hour_offset
#    print str(month)+"/"+str(day) + "/"+str(year)+\
#          " "+str(hour).zfill(2)+":"+str(minute).zfill(2)\
#    +" \t"+self.binary[print_offset:print_offset+5]+"   "\
#      +self.bin_str()
    if year != 14 or month > 12 or month < 1 or day > 28 or day < 1 or\
      hour >= 24 or minute >= 60:
      self.is_valid_record = False
      return
    return datetime(year, month, day, hour, minute)

  def bin_str(self):
    string = ""
    for i in range(0, 7):
      string += self.binary[i*8:(i+1)*8] + "-"
    return string

  def str(self):
    if self.is_valid_record:
      return "Record "+self.op_code+": "+str(self.mydatetime)+" - "\
      +self.raw+" - "+self.binary
      #     +" - "+str(self.bwdatetime)
    else:
      return "This is an invalid record: "+self.binary


############# Main #################
fileInName = "ReadHistoryData-page-0.data.hex"

with open (fileInName, "r") as myfile:
    data=myfile.read().replace('\n', '')

op_codes = []
for i in range(256):
  op_code = i #= int(data[i:i+2], 16)
  op_codes.append(op_code_stats(op_code, data))

op_codes = sorted(op_codes, key=lambda op_code_stats: op_code_stats.num_records)

#for op_code in op_codes:
#  if op_code.is_likely_op():
#    print op_code.str()

import array
from times import *
from datetime import *
op_code = 11 # 11=0b
#op_code = 10 # 10=0a
print "\n\n"
records = data.split('{0:02x}'.format(op_code))
parsed_records = []
for package in records:
  record_len = len(package)
  if len(package) == 14:
    parsed_records.append(record("0b", package))

valid_records = []
for record in parsed_records:
  if record.is_valid_record:
    valid_records.append(record)

print "should match about 284 parsed("+ str(len(parsed_records))+") valid("+\
  str(len(valid_records))+")"

valid_records.sort(key=lambda r:r.mydatetime)

for record in valid_records:
  print record.str()
