#!/usr/bin/python

from binascii import hexlify
from datetime import datetime
from pprint import pformat

import json
import difflib

from times import *
from bolus import *

# I don't know where else to put this.
"""
    #
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ ])
    + bytearray([ ])),
"""

_midnights = {
  'page_4': [
    # record 14 (2013, 0, 7, 6, 5, 0)
    # 1/8/13 00:00:00,34.9,ResultDailyTotal,"AMOUNT=34.9,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x26, 0x07, 0x8d, ])
    + bytearray([ 0x6d, 0x07, 0x8d, 0x05, 0x00, 0x94, 0x58, 0xd8,
                  0x07, 0x00, 0x00, 0x05, 0x26, 0x03, 0x72, 0x43,
                  0x01, 0xb4, 0x21, 0x00, 0x79, 0x01, 0xb4, 0x21,
                  0x01, 0x64, 0x52, 0x00, 0x50, 0x12, 0x00, 0x00,
                  0x00, 0x05, 0x04, 0x01, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record 30 (2013, 0, 8, 20, 5, 0)
    # 1/9/13 00:00:00,27.4,ResultDailyTotal,"AMOUNT=27.35,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x74, 0x08, 0x8d, ])
    + bytearray([ 0x6d, 0x08, 0x8d, 0x05, 0x10, 0xf6, 0x8e, 0x8f,
                  0x05, 0x00, 0x00, 0x05, 0x74, 0x03, 0x74, 0x3f,
                  0x02, 0x00, 0x25, 0x00, 0x35, 0x02, 0x00, 0x25,
                  0x00, 0xa0, 0x1f, 0x01, 0x60, 0x45, 0x00, 0x00,
                  0x00, 0x04, 0x00, 0x03, 0x01, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record (2013, 0, 9, 6, 4, 0)
    # 1/10/13 00:00:00,33.2,ResultDailyTotal,"AMOUNT=33.15,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x04, 0x46, 0x09, 0x8d, ])
    + bytearray([ 0x6d, 0x09, 0x8d, 0x05, 0x10, 0xd3, 0x62, 0x29,
                  0x03, 0x00, 0x00, 0x04, 0x46, 0x03, 0x76, 0x51,
                  0x00, 0xd0, 0x13, 0x00, 0x2c, 0x00, 0xd0, 0x13,
                  0x00, 0x7c, 0x3c, 0x00, 0x54, 0x28, 0x00, 0x00,
                  0x00, 0x02, 0x01, 0x01, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),
  ],

  'page_14': [
    # record 8 (2012, 0, 2, 6, 6, 0)
    # 12/3/12 00:00:00,32.3,ResultDailyTotal,"AMOUNT=32.3,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x06, 0x06, 0xc2, 0x0c, ])
    + bytearray([ 0x6d, 0xc2, 0x0c, 0x05, 0x10, 0xb1, 0x60, 0x8b,
    0x09, 0x00, 0x00, 0x06, 0x06, 0x03, 0x7c, 0x3a,
    0x02, 0x8a, 0x2a, 0x00, 0x64, 0x02, 0x8a, 0x2a,
    0x01, 0x2e, 0x2e, 0x01, 0x5c, 0x36, 0x00, 0x00,
    0x00, 0x07, 0x03, 0x04, 0x00, 0x00, 0x0c, 0x00,
    0xe8, 0x00, 0x00, 0x00, ])),

    # record 22 (2012, 0, 3, 12, 5, 0)
    # 12/4/12 00:00:00,36.0,ResultDailyTotal,"AMOUNT=35.95,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x0c, 0xc3, 0x0c, ])
    + bytearray([ 0x6d, 0xc3, 0x0c, 0x05, 0x10, 0xb7, 0x4d, 0x14,
                  0x03, 0x00, 0x00, 0x05, 0x0c, 0x03, 0x7c, 0x45,
                  0x01, 0x90, 0x1f, 0x00, 0x5f, 0x01, 0x90, 0x1f,
                  0x01, 0x04, 0x41, 0x00, 0x8c, 0x23, 0x00, 0x00,
                  0x00, 0x04, 0x03, 0x01, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record 35 (2012, 0, 4, 30, 5, 0)
    # 12/5/12 00:00:00,25.9,ResultDailyTotal,"AMOUNT=25.9,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x9e, 0xc4, 0x0c, ])
    + bytearray([ 0x6d, 0xc4, 0x0c, 0x05, 0x00, 0xaa, 0x89, 0xc6,
    0x03, 0x00, 0x00, 0x05, 0x9e, 0x03, 0x76, 0x3e,
    0x02, 0x28, 0x26, 0x00, 0x8f, 0x02, 0x28, 0x26,
    0x01, 0xb0, 0x4e, 0x00, 0x78, 0x16, 0x00, 0x00,
    0x00, 0x05, 0x03, 0x02, 0x00, 0x00, 0x0c, 0x00,
    0xe8, 0x00, 0x00, 0x00, ])),

  ],

  'page_29': [
    # record 9 (2012, 0, 8, 28, 5, 0)
    # 10/9/12 00:00:00,34.8,ResultDailyTotal,"AMOUNT=34.85,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x9c, 0xa8, 0x0c, ])
    + bytearray([ 0x6d, 0xa8, 0x0c, 0x05, 0x10, 0xab, 0x61, 0x1a,
                  0x03, 0x00, 0x00, 0x05, 0x9c, 0x03, 0x78, 0x3e,
                  0x02, 0x24, 0x26, 0x00, 0x8b, 0x02, 0x24, 0x26,
                  0x01, 0x9c, 0x4b, 0x00, 0x88, 0x19, 0x00, 0x00,
                  0x00, 0x04, 0x03, 0x01, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record 24 (2012, 0, 9, 18, 5, 0)
    # 10/10/12 00:00:00,30.8,ResultDailyTotal,"AMOUNT=30.85,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x72, 0xa9, 0x0c, ])
    + bytearray([ 0x6d, 0xa9, 0x0c, 0x05, 0x00, 0x96, 0x73, 0xb6,
                  0x03, 0x00, 0x00, 0x05, 0x72, 0x03, 0x76, 0x40,
                  0x01, 0xfc, 0x24, 0x00, 0x91, 0x01, 0xfc, 0x24,
                  0x01, 0xb4, 0x56, 0x00, 0x48, 0x0e, 0x00, 0x00,
                  0x00, 0x07, 0x05, 0x02, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record 39  (2012, 0, 10, 18, 4, 0)
    # 10/11/12 00:00:00,30.2,ResultDailyTotal,"AMOUNT=30.2,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x04, 0xd2, 0xaa, 0x0c, ])
    + bytearray([ 0x6d, 0xaa, 0x0c, 0x05, 0x10, 0xb6, 0x8d, 0x23,
                  0x05, 0x00, 0x00, 0x04, 0xd2, 0x03, 0x72, 0x47,
                  0x01, 0x60, 0x1d, 0x00, 0x36, 0x01, 0x60, 0x1d,
                  0x00, 0xa0, 0x2d, 0x00, 0xc0, 0x37, 0x00, 0x00,
                  0x00, 0x04, 0x02, 0x02, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),
  ],
  'page_35': [
    # record 2 (2012, 0, 13, 22, 4, 0)
    # 9/14/12 00:00:00,31.2,ResultDailyTotal,"AMOUNT=31.2,
    # CONCENTRATION=null"
    #
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x04, 0x96, 0x8d, 0x8c, ])
    + bytearray([ 0x6d, 0x8d, 0x8c, 0x05, 0x00, 0x80, 0x68, 0x97,
                  0x02, 0x00, 0x00, 0x04, 0x96, 0x03, 0x42, 0x47,
                  0x01, 0x54, 0x1d, 0x00, 0x6d, 0x01, 0x54, 0x1d,
                  0x01, 0x40, 0x5e, 0x00, 0x14, 0x06, 0x00, 0x00,
                  0x00, 0x05, 0x04, 0x01, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # record 18  (2012, 0, 14, 0, 4, 0)
    # correct is 9/15/12 00:00:00,28.2,ResultDailyTotal,"AMOUNT=28.15,
    # CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x04, 0xe0, 0x8e, 0x8c, ])
    + bytearray([ 0x6d, 0x8e, 0x8c, 0x05, 0x00, 0x74, 0x66, 0x8e,
                  0x07, 0x00, 0x00, 0x04, 0xe0, 0x03, 0x74, 0x47,
                  0x01, 0x6c, 0x1d, 0x00, 0x7b, 0x01, 0x6c, 0x1d,
                  0x01, 0x6c, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x05, 0x05, 0x00, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # correct is something like: (2012, 0, 15, 6, 4, 0)
    # 2012-09:15T00:00:00 or
    # 2012-09-16T24:00:00
    # 32.8,ResultDailyTotal,"AMOUNT=32.8, CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x04, 0x66, 0x8f, 0x8c, ])
    + bytearray([ 0x6d, 0x8f, 0x8c, 0x05, 0x00, 0x80, 0x42, 0xf2,
                  0x05, 0x00, 0x00, 0x04, 0x66, 0x03, 0x56, 0x4c,
                  0x01, 0x10, 0x18, 0x00, 0x5b, 0x01, 0x10, 0x18,
                  0x01, 0x10, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00,
                  0x00, 0x02, 0x02, 0x00, 0x00, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ])),

    # correct is something like: (2012, 0, 16, 0, 5, 0))
    # 2012-09-16T24:00:00 or
    # 2012-09:17T00:00:00
    # 32.2,ResultDailyTotal,"AMOUNT=32.2, CONCENTRATION=null"
    ( bytearray([ 0x07, 0x00 ])
    + bytearray([ 0x00, 0x05, 0x20, 0x90, 0x8c ])
    + bytearray([ 0x6d, 0x90, 0x8c, 0x05, 0x00, 0x89, 0x6c, 0xaa,
                  0x03, 0x00, 0x00, 0x05, 0x20, 0x03, 0x78, 0x44,
                  0x01, 0xa8, 0x20, 0x00, 0x7e, 0x01, 0xa8, 0x20,
                  0x01, 0x80, 0x5b, 0x00, 0x28, 0x09, 0x00, 0x00,
                  0x00, 0x05, 0x03, 0x01, 0x01, 0x00, 0x0c, 0x00,
                  0xe8, 0x00, 0x00, 0x00, ]))
  ],
}

_bewest_dates = {
  # from https://github.com/bewest/decoding-carelink/blob/rewriting/analysis/bewest-pump/ReadHistoryData-page-19.data.list_opcodes.markdown
  'page-19': {
    0:  [ 0xaa, 0xf7, 0x40, 0x0c, 0x0c, ],
    1:  [ 0x40, 0x0c, 0x0c, 0x0a, 0x0c, ],
    2:  [ 0x0c, 0x8b, 0xc3, 0x28, 0x0c, ],
    3:  [ 0x8b, 0xc3, 0x28, 0x0c, 0x8c, ],
    4:  [ 0x28, 0x0c, 0x8c, 0x5b, 0x0c, ],
    5:  [ 0x8d, 0xc3, 0x08, 0x0c, 0x0c, ],
    6:  [ 0xaa, 0xf7, 0x00, 0x0c, 0x0c, ],
  }
}

def _test_decode_bolus( ):
  """
  ## correct
  >>> parse_date( bytearray( _bewest_dates['page-19'][6] ) ).isoformat( )
  '2012-11-12T00:55:42'

  ## correct
  >>> parse_date( bytearray( _bewest_dates['page-19'][0] ) ).isoformat( )
  '2012-11-12T00:55:42'

  ## this is wrong
  >>> parse_date( bytearray( _bewest_dates['page-19'][1] ) ).isoformat( )
  '2012-04-10T12:12:00'

  ## day,month is wrong, time H:M:S is correct
  # expected:
  >>> parse_date( bytearray( _bewest_dates['page-19'][2] ) ).isoformat( )
  '2012-02-08T03:11:12'

  ## correct
  >>> parse_date( bytearray( _bewest_dates['page-19'][3] ) ).isoformat( )
  '2012-11-12T08:03:11'

  #### not a valid date
  # >>> parse_date( bytearray( _bewest_dates['page-19'][4] ) ).isoformat( )

  ## correct
  >>> parse_date( bytearray( _bewest_dates['page-19'][5] ) ).isoformat( )
  '2012-11-12T08:03:13'


  """
  """

  0x5b 0x7e # bolus wizard,
  0xaa 0xf7 0x00 0x0c 0x0c # page-19[0]

  0x0f 0x50 0x0d 0x2d 0x6a 0x00 0x0b 0x00
  0x00 0x07 0x00 0x0b 0x7d 0x5c 0x08 0x58
  0x97 0x04 0x30 0x05 0x14 0x34 0xc8
  0x91 0xf8      # 0x91, 0xf8 = month=11, minute=56, seconds=17!
  0x00           # general parsing fails here
  0x00
  0xaa 0xf7 0x40 0x0c 0x0c # expected  - page-19[6]

  0x0a 0x0c
  0x8b 0xc3 0x28 0x0c 0x8c # page-19[3]


  0x5b 0x0c

  0x8d 0xc3 0x08 0x0c 0x0c # page-19[5]
  0x00 0x51 0x0d 0x2d 0x6a 0x1f 0x00 0x00 0x00 0x00 0x00
  """

### csv deconstructed
"""
395,11/12/12,00:55:42,11/12/12 00:55:42,Normal 1.1,1.1,BolusNormal
  "AMOUNT=1.1, CONCENTRATION=null, PROGRAMMED_AMOUNT=1.1,
  ACTION_REQUESTOR=pump, ENABLE=true, IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    9942920032,51974238,2086,Paradigm 522

396,11/12/12,00:56:17,11/12/12 00:56:17 JournalEntryPumpLowReservoir
  "AMOUNT=20, ACTION_REQUESTOR=pump"
    9942920033,51974238,2087,Paradigm 522


397,11/12/12,08:03:11,11/12/12 08:03:11 268 CalBGForPH
  "AMOUNT=268, ACTION_REQUESTOR=pump"
    9942920031,51974238,2085,Paradigm 522

398,11/12/12,08:03:13,11/12/12 08:03:13 UnabsorbedInsulin
  "BOLUS_ESTIMATE_DATUM=9942920029, INDEX=0, AMOUNT=1.1, RECORD_AGE=429,
  INSULIN_TYPE=null,
  INSULIN_ACTION_CURVE=240"
    9942920030,51974238,2084,Paradigm 522

399,11/12/12,08:03:13,11/12/12 08:03:13
  3.1,125,106,13,45,0,268,3.1,0,0.0
  BolusWizardBolusEstimate,"BG_INPUT=268, BG_UNITS=mg dl,
  CARB_INPUT=0, CARB_UNITS=grams, CARB_RATIO=13,
  INSULIN_SENSITIVITY=45, BG_TARGET_LOW=106, BG_TARGET_HIGH=125,
  BOLUS_ESTIMATE=3.1, CORRECTION_ESTIMATE=3.1, FOOD_ESTIMATE=0,
  UNABSORBED_INSULIN_TOTAL=0, UNABSORBED_INSULIN_COUNT=1,
  ACTION_REQUESTOR=pump"
    9942920029,51974238,2083,Paradigm 522

400,11/12/12,08:03:13,11/12/12 08:03:13 Normal
  3.1,3.1 BolusNormal "AMOUNT=3.1, CONCENTRATION=null,
  PROGRAMMED_AMOUNT=3.1, ACTION_REQUESTOR=pump, ENABLE=true,
  IS_DUAL_COMPONENT=false,
  UNABSORBED_INSULIN_TOTAL=null"
    9942920028,51974238,2082,Paradigm 522

401,11/12/12,08:50:31,11/12/12 08:50:31 JournalEntryPumpLowReservoir
  "AMOUNT=10, ACTION_REQUESTOR=pump"
    9942920027,51974238,2081,Paradigm 522

"""



_bad_days = [
    bytearray([ 0xa9, 0xf5, 0x15, 0x14, 0x0c, ]),
    bytearray([ 0xa6, 0xc7, 0x36, 0x14, 0x8c, ]),
    bytearray([ 0xa9, 0xf5, 0x15, 0x14, 0x0c, ]),
    bytearray([ 0xa6, 0xc7, 0x36, 0x14, 0x8c, ]),

    bytearray([ 0xa2, 0xe9, 0x10, 0x19, 0x0c, ]),
    bytearray([ 0xa0, 0xf6, 0x0d, 0x19, 0x0c, ]),
    bytearray([ 0xa5, 0xd9, 0x34, 0x1d, 0x0c, ]),

    bytearray([ 0xc2, 0x3b, 0x0e, 0x14, 0x0c, ]),
    bytearray([ 0xd9, 0x1c, 0x0f, 0x14, 0x0c, ]),
  ]

# days need 5 bits
def big_days(x=0):
  """
    # page 17, RECORD 11
    >>> parse_date( big_days(0) ).isoformat( )
    '2012-11-20T21:53:41'

    # page 17, ~ RECORD 12
    >>> parse_date( big_days(1) ).isoformat( )
    '2012-11-20T22:07:38'

    >>> parse_date( big_days(2) ).isoformat( )
    '2012-11-20T21:53:41'

    >>> parse_date( big_days(3) ).isoformat( )
    '2012-11-20T22:07:38'

    # page 16, RECORD ~15
    >>> parse_date( big_days(4) ).isoformat( )
    '2012-11-25T16:41:34'

    >>> parse_date( big_days(5) ).isoformat( )
    '2012-11-25T13:54:32'

    # page 15
    >>> parse_date( big_days(6) ).isoformat( )
    '2012-11-29T20:25:37'

    # page 0
    >>> parse_date( big_days(7) ).isoformat( )
    '2012-12-20T14:59:02'

    >>> parse_date( big_days(8) ).isoformat( )
    '2012-12-20T15:28:25'

  """
  return _bad_days[x]


_wizards = [
  # 2382,1/19/13,21:50:15,1/19/13
  # 21:50:15,5.9,125,106,13,45,87,75,-0.7,6.6,0.0,BolusWizardBolusEstimate,"BG_INPUT=75,
  # BG_UNITS=mg dl, CARB_INPUT=87, CARB_UNITS=grams, CARB_RATIO=13,
  # INSULIN_SENSITIVITY=45, BG_TARGET_LOW=106, BG_TARGET_HIGH=125,
  # BOLUS_ESTIMATE=5.9, CORRECTION_ESTIMATE=-0.7, FOOD_ESTIMATE=6.6,
  # UNABSORBED_INSULIN_TOTAL=0, UNABSORBED_INSULIN_COUNT=0,
  # ACTION_REQUESTOR=pump"
  # 9942918055,51974238,109,Paradigm 522
  bytearray([ 0x5b, 0x4b,
              0x0f, 0x72, 0x15, 0x13, 0x0d,
              0x57, 0x50, 0x0d, 0x2d, 0x6a, 0xf9, 0x42, 0xf0,
              0x00, 0x00, 0x00, 0x3b, 0x7d, ]),

  # 2295,1/14/13,22:36:00,1/14/13
  # 22:36:00,6.7,125,106,13,45,94,83,-0.5,7.2,1.0,BolusWizardBolusEstimate,"BG_INPUT=83,
  # BG_UNITS=mg dl, CARB_INPUT=94, CARB_UNITS=grams, CARB_RATIO=13,
  # INSULIN_SENSITIVITY=45, BG_TARGET_LOW=106, BG_TARGET_HIGH=125,
  # BOLUS_ESTIMATE=6.7, CORRECTION_ESTIMATE=-0.5, FOOD_ESTIMATE=7.2,
  # UNABSORBED_INSULIN_TOTAL=1, UNABSORBED_INSULIN_COUNT=8,
  # ACTION_REQUESTOR=pump"
  #  9942918140,51974238,194,Paradigm 522
  bytearray([ 0x5b, 0x53,
              0x00, 0x64, 0x16, 0x0e, 0x0d,
              0x5e, 0x50, 0x0d, 0x2d, 0x6a, 0xfb, 0x48, 0xf0,
              0x00, 0x0a, 0x00, 0x43, 0x7d, ]),
  # bytearray([ ]),
]

from decocare import models
model522 = models.PumpModel('522', None)
def _test_bolus_wizards( ):
  """
  >>> rec = BolusWizard( _wizards[0][:2], model522 )
  >>> print pformat(rec.parse( _wizards[0] ))
  {'_byte[5]': 249,
   '_byte[7]': 240,
   'bg': 75,
   'bg_target_high': 125,
   'bg_target_low': 106,
   'bolus_estimate': 5.9,
   'carb_input': 87,
   'carb_ratio': 13,
   'correction_estimate': -0.7,
   'food_estimate': 6.6,
   'sensitivity': 45,
   'unabsorbed_insulin_count': '??',
   'unabsorbed_insulin_total': 0.0,
   'unknown_byte[10]': 0,
   'unknown_byte[8]': 0}
  >>> print str(rec)
  BolusWizard 2013-01-19T21:50:15 head[2], body[13] op[0x5b]


  >>> rec = BolusWizard( _wizards[1][:2], model522 )
  >>> print pformat(rec.parse( _wizards[1] ))
  {'_byte[5]': 251,
   '_byte[7]': 240,
   'bg': 83,
   'bg_target_high': 125,
   'bg_target_low': 106,
   'bolus_estimate': 6.7,
   'carb_input': 94,
   'carb_ratio': 13,
   'correction_estimate': -0.5,
   'food_estimate': 7.2,
   'sensitivity': 45,
   'unabsorbed_insulin_count': '??',
   'unabsorbed_insulin_total': 1.0,
   'unknown_byte[10]': 0,
   'unknown_byte[8]': 0}

  >>> print str(rec)
  BolusWizard 2013-01-14T22:36:00 head[2], body[13] op[0x5b]

  """
  pass


_bolus = [

  # 2381,1/19/13,21:50:15,1/19/13
  # 21:50:15,Dual/Normal,2.6,2.6,BolusNormal,"AMOUNT=2.6,
  # CONCENTRATION=null, PROGRAMMED_AMOUNT=2.6, ACTION_REQUESTOR=pump,
  # ENABLE=true, IS_DUAL_COMPONENT=true,
  # UNABSORBED_INSULIN_TOTAL=null"
  #  9942918054,51974238,108,Paradigm 522
  bytearray([ 0x01, 0x1a, 0x1a, 0x00,
              0x0f, 0x72, 0x95, 0x13, 0x0d, ]),

  # 2305,1/15/13,15:57:16,1/15/13
  # 15:57:16,Normal,1.7,1.7,BolusNormal,"AMOUNT=1.7,
  # CONCENTRATION=null, PROGRAMMED_AMOUNT=1.7, ACTION_REQUESTOR=pump,
  # ENABLE=true, IS_DUAL_COMPONENT=false,
  # UNABSORBED_INSULIN_TOTAL=null"
  #  9942918131,51974238,185,Paradigm 522
  bytearray([ 0x01, 0x11, 0x11, 0x00,
              0x10, 0x79, 0x4f, 0x0f, 0x0d, ]),
  # bytearray([ ]),

]

def _test_bolus( ):
  """
  >>> rec = Bolus( _bolus[0][:2] )
  >>> print pformat(rec.parse( _bolus[0] ))
  {'amount': 2.6, 'duration': 0, 'programmed': 2.6, 'type': 'normal'}

  >>> print str(rec)
  Bolus 2013-01-19T21:50:15 head[4], body[0] op[0x01]

  >>> rec = Bolus( _bolus[1][:2] )
  >>> print pformat(rec.parse( _bolus[1] ))
  {'amount': 1.7, 'duration': 0, 'programmed': 1.7, 'type': 'normal'}
  >>> print str(rec)
  Bolus 2013-01-15T15:57:16 head[4], body[0] op[0x01]

  """

class TestSaraBolus:
  # model 722
  hexdump = """
  5b 67
    a1 51 0e 04 0d
    0d 50 00 78
  3c 64 00 00 28 00 00 14 00 28 78
  5c 08 44 79 c0 3c 4b d0
  01 00 28 00 28 00 14 00
    a1 51 4e 04 0d
  0a fc
    b4 54 2f 04 0d
  5b fc
    b7 54 0f 04 0d
    00 50 00 78
  3c 64 58 00 00 00 00 1c 00 3c 78
  5c 0b 28 40 c0 44 b8 c0 3c 8a d0
  01 00 3c 00 3c 00 1c 00
    b7 54 4f 04 0d
  """
  csv_breakdown = """
  9/4/13 14:17:33,,,,,,,Normal,1.0,1.0,,,,,,,,,,,,,,,,,,,,,BolusNormal
    "AMOUNT=1
      CONCENTRATION=null
      PROGRAMMED_AMOUNT=1
      ACTION_REQUESTOR=pump
      ENABLE=true
      IS_DUAL_COMPONENT=false
      UNABSORBED_INSULIN_TOTAL=0.5"
    11345487207,52554138,86,Paradigm Revel - 723

  9/4/13 14:17:33,,,,,,,,,,,,,,,1.0,120,100,12,60,13,103,0,1,0.5,,,,,,BolusWizardBolusEstimate,"BG_INPUT=103
      BG_UNITS=mg dl
      CARB_INPUT=13
      CARB_UNITS=grams
      CARB_RATIO=12
      INSULIN_SENSITIVITY=60
      BG_TARGET_LOW=100
      BG_TARGET_HIGH=120
      BOLUS_ESTIMATE=1
      CORRECTION_ESTIMATE=0
      FOOD_ESTIMATE=1
      UNABSORBED_INSULIN_TOTAL=0.5
      UNABSORBED_INSULIN_COUNT=2
      ACTION_REQUESTOR=pump"
    11345487208,52554138,87,Paradigm Revel - 723

  9/4/13 14:17:33,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,UnabsorbedInsulin,"BOLUS_ESTIMATE_DATUM=11345487208
      INDEX=0
      AMOUNT=1.7
      RECORD_AGE=121
      INSULIN_TYPE=null
      INSULIN_ACTION_CURVE=180"
    11345487209,52554138,88,Paradigm Revel - 723

  9/4/13 14:17:33,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,UnabsorbedInsulin,"BOLUS_ESTIMATE_DATUM=11345487208
      INDEX=1
      AMOUNT=1.5
      RECORD_AGE=331
      INSULIN_TYPE=null
      INSULIN_ACTION_CURVE=180"
    11345487210,52554138,89,Paradigm Revel - 723

  9/4/13 15:20:52,,,,,,,,,,,,,,,,,,,,,,,,,,252,,,,CalBGForPH,"AMOUNT=252, ACTION_REQUESTOR=pump"
    11345487206,52554138,85,Paradigm Revel - 723

  9/4/13 15:20:55,,,,,,,Normal,1.5,1.5,,,,,,,,,,,,,,,,,,,,,BolusNormal,"AMOUNT=1.5
      CONCENTRATION=null
      PROGRAMMED_AMOUNT=1.5
      ACTION_REQUESTOR=pump
      ENABLE=true
      IS_DUAL_COMPONENT=false
      UNABSORBED_INSULIN_TOTAL=0.7"
    11345487201,52554138,80,Paradigm Revel - 723

  9/4/13 15:20:55,,,,,,,,,,,,,,,1.5,120,100,12,60,0,252,2.2,0,0.7,,,,,,BolusWizardBolusEstimate,"BG_INPUT=252
      BG_UNITS=mg dl
      CARB_INPUT=0
      CARB_UNITS=grams
      CARB_RATIO=12
      INSULIN_SENSITIVITY=60
      BG_TARGET_LOW=100
      BG_TARGET_HIGH=120
      BOLUS_ESTIMATE=1.5
      CORRECTION_ESTIMATE=2.2
      FOOD_ESTIMATE=0
      UNABSORBED_INSULIN_TOTAL=0.7
      UNABSORBED_INSULIN_COUNT=3
      ACTION_REQUESTOR=pump"
    11345487202,52554138,81,Paradigm Revel - 723

  9/4/13 15:20:55,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,UnabsorbedInsulin,"BOLUS_ESTIMATE_DATUM=11345487202
      INDEX=0
      AMOUNT=1
      RECORD_AGE=64
      INSULIN_TYPE=null
      INSULIN_ACTION_CURVE=180"
    11345487203,52554138,82,Paradigm Revel - 723

  9/4/13 15:20:55,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,UnabsorbedInsulin,"BOLUS_ESTIMATE_DATUM=11345487202
      INDEX=1
      AMOUNT=1.7
      RECORD_AGE=184
      INSULIN_TYPE=null
      INSULIN_ACTION_CURVE=180"
    11345487204,52554138,83,Paradigm Revel - 723

  9/4/13 15:20:55,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,UnabsorbedInsulin,"BOLUS_ESTIMATE_DATUM=11345487202
      INDEX=2
      AMOUNT=1.5
      RECORD_AGE=394
      INSULIN_TYPE=null
      INSULIN_ACTION_CURVE=180"
    11345487205,52554138,84,Paradigm Revel - 723
  9/4/13 16:11:57,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentSensorMissedDataTime,TIME=1800000,11345487185,52554138,64,Paradigm Revel - 723
  """
  bolus_1_ok = {
      'bg': 103,
      # 'BG_UNITS': 'mg dl'
      'carb_input': 13,
      #'CARB_UNITS': 'grams',
      'carb_ratio': 12,
      'sensitivity': 60,
      'bg_target_low': 100,
      'bg_target_high': 120,
      'bolus_estimate': 1,
      'correction_estimate': 0,
      'food_estimate': 1,
      'unabsorbed_insulin_total': 0.5,
      'unabsorbed_insulin_count': 2,
      #'action_requestor': 'pump'
  }
  bw_1_bytes = bytearray(''.join("""
  5b 67
    a1 51 0e 04 0d
    0d 50 00 78
    3c 64 00 00 28 00 00 14 00 28 78
  """.strip( ).split( )).decode('hex'))
  bw_2_bytes = bytearray(''.join("""
  5b fc
    b7 54 0f 04 0d
    00 50 00 78
    3c 64 58 00 00 00 00 1c 00 3c 78
  """.strip( ).split( )).decode('hex'))

  cal_bg_bytes = bytearray(''.join("""
  0a fc
    b4 54 2f 04 0d
  """.strip( ).split( )).decode('hex'))
  @classmethod
  def test_cal_bg(klass):
    """
    >>> TestSaraBolus.test_cal_bg( )
    CalBGForPH 2013-09-04T15:20:52 head[2], body[0] op[0x0a]
    {
      "amount": 252
    }
    """
    # 9/4/13 15:20:52,,,,,,,,,,,,,,,,,,,,,,,,,,252,,,,CalBGForPH,"AMOUNT=252, ACTION_REQUESTOR=pump"
    data = klass.cal_bg_bytes
    rec = CalBGForPH(data[:2])
    d = rec.parse(data)
    print str(rec)
    print json.dumps(d, indent=2)

def dictlines(d):
  items = d.items( )
  items.sort( )
  d = [ "%s: %s\n" % (k, v) for (k, v) in items ]
  return d

def unsolved_bolus_wizard( ):
  """
  # >>> unsolved_bolus_wizard( )
  """
  # these byte sequences line up with these records:
  bw_ok_1 = {
      'bg_input': 103,
      'carb_input': 13,
      'carb_ratio': 12,
      'insulin_sensitivity': 60,
      'bg_target_low': 100,
      'bg_target_high': 120,
      'bolus_estimate': 1,
      'correction_estimate': 0,
      'food_estimate': 1,
      'unabsorbed_insulin_total': 0.5,
      'unabsorbed_insulin_count': 2,
  }
  bw_ok_2 = {
      'bg_input': 252,
      'carb_input': 0,
      'carb_ratio': 12,
      'insulin_sensitivity': 60,
      'bg_target_low': 100,
      'bg_target_high': 120,
      'bolus_estimate': 1.5,
      'correction_estimate': 2.2,
      'food_estimate': 0,
      'unabsorbed_insulin_total': 0.7,
      'unabsorbed_insulin_count': 3,
  }
  found = decode_wizard(TestSaraBolus.bw_1_bytes)
  if found != bw_ok_1:
    print "FOUND:"
    print json.dumps(found, indent=2)
    print "EXPECTED:"
    print json.dumps(bw_ok_1, indent=2)
  found = decode_wizard(TestSaraBolus.bw_2_bytes)
  if found != bw_ok_2:
    print "FOUND:"
    print json.dumps(found, indent=2)
    print "EXPECTED:"
    print json.dumps(bw_ok_2, indent=2)

def decode_wizard(data):
  """
  BYTE
  01:
  02:
  03:
  04:
  05:
  06:
  07:
  08:
  09:
  10:
  12:
  13:
  14:
  15:
  16:
  17:
  18:
  19:
  20:
  21:
  22:
  """
  head = data[:2]
  date = data[2:7]
  datetime = parse_date(date)
  body = data[7:]
  bg = lib.BangInt([ body[1] & 0x0f, head[1] ])
  carb_input = int(body[0])
  carb_ratio = int(body[2])
  bg_target_low = int(body[5])
  bg_target_high = int(body[3])
  sensitivity = int(body[4])

  print "BOLUS WIZARD", datetime.isoformat( )
  wizard = { 'bg_input': bg, 'carb_input': carb_input,
             'carb_ratio': carb_ratio,
             'insulin_sensitivity': sensitivity,
             'bg_target_low': bg_target_low,
             'bg_target_high': bg_target_high,
  }
  return wizard

class BW722(BolusWizard):
  def decode(self):
    self.parse_time( )
    bg = lib.BangInt([ self.body[1] & 0x0f, self.head[1] ])
    carb_input = int(self.body[0])
    carb_ratio = int(self.body[2])
    bg_target_low = int(self.body[5])
    bg_target_high = int(self.body[3])
    sensitivity = int(self.body[12])

    # XXX: Most likely incorrect.
    correction = ( twos_comp( self.body[7], 8 )
                 + twos_comp( self.body[5] & 0x0f, 8 ) ) / 10.0
    wizard = { 'bg': bg, 'carb_input': carb_input,
               'carb_ratio': carb_ratio,
               'sensitivity': sensitivity,
               'bg_target_low': bg_target_low,
               'bg_target_high': bg_target_high,
               #'bolus_estimate': int(self.body[6])/10.0,
               #'food_estimate': int(self.body[13])/10.0,
               #'unabsorbed_insulin_total': int(self.body[9])/10.0,
               #'unabsorbed_insulin_count': self.body[11],
               'correction_estimate': correction,
               # '??': '??',
               # 'unabsorbed_insulin_total': int(self.body[9])/10.0,
               # 'food_estimate': int(self.body[0]),
             }
    return wizard



if __name__ == '__main__':
  import doctest
  doctest.testmod( )

#####
# EOF
