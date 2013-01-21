
# what do midnight records look like?


#### RECORD 2 Prime 2006-10-04T08:11:21 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x00 0x00 0x0d                   .....
    decimal
              3    0    0    0   13
    datetime (2006-10-04T08:11:21)
    0000   0x95 0x8b 0x28 0x04 0x06                   ..(..
    body (0)

I can't find this time anywhere in the CSV.
I do see this:
```
06,18:29:32,7/2/06 18:29:32,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9779565961,51910876,0,Paradigm 515
06,18:37:22,7/2/06 18:37:22,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9779570111,51910881,0,Paradigm 515
06,18:57:35,7/2/06 18:57:35,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9779598493,51910796,0,Paradigm 515
06,00:00:00,7/3/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,20.6,ResultDailyTotal,"AMOUNT=20.55, CONCENTRATION=null",9799981773,51919235,114,Paradigm 515
06,10:00:14,7/3/06 10:00:14,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9782871710,51912274,0,Paradigm 515
06,00:00:00,7/4/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,20.6,ResultDailyTotal,"AMOUNT=20.55, CONCENTRATION=null",9799981772,51919235,113,Paradigm 515
06,00:00:00,7/5/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,20.6,ResultDailyTotal,"AMOUNT=20.55, CONCENTRATION=null",9799981771,51919235,112,Paradigm 515
06,00:00:00,7/6/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,20.6,ResultDailyTotal,"AMOUNT=20.55, CONCENTRATION=null",9799981769,51919235,110,Paradigm 515
06,00:00:00,7/7/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,21.7,ResultDailyTotal,"AMOUNT=21.7, CONCENTRATION=null",9801076688,51919644,97,Paradigm 515
06,16:48:52,7/7/06 16:48:52,,,,,,,,,,,Manual,1.9,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=1.9, CONCENTRATION=null, PROGRAMMED_AMOUNT=0, PRIME_TYPE=manual, ACTION_REQUESTOR=pump",9799981761,51919235,102,Paradigm 515
06,16:49:12,7/7/06 16:49:12,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981760,51919235,101,Paradigm 515
06,17:10:38,7/7/06 17:10:38,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981759,51919235,100,Paradigm 515
06,17:28:51,7/7/06 17:28:51,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981758,51919235,99,Paradigm 515
06,17:41:14,7/7/06 17:41:14,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981757,51919235,98,Paradigm 515
06,17:57:02,7/7/06 17:57:02,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981756,51919235,97,Paradigm 515
06,18:02:05,7/7/06 18:02:05,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9799981755,51919235,96,Paradigm 515
06,18:22:31,7/7/06 18:22:31,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9799981659,51919235,0,Paradigm 515
06,00:00:00,7/8/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,2.2,ResultDailyTotal,"AMOUNT=2.2, CONCENTRATION=null",9801773188,51920003,101,Paradigm 515
06,05:22:49,7/8/06 05:22:49,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9801076687,51919644,96,Paradigm 515
06,05:49:06,7/8/06 05:49:06,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9801076591,51919644,0,Paradigm 515
06,07:11:37,7/8/06 07:11:37,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ChangeTimeDisplayFormat,"FORMAT=d12, ACTION_REQUESTOR=pump",9801773190,51920003,103,Paradigm 515
06,07:12:12,7/8/06 07:12:12,8/31/06 23:30:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ChangeTime,"NEW_TIME=1157067000000, ACTION_REQUESTOR=pump",9801773189,51920003,102,Paradigm 515
/06,00:00:00,8/31/06 00:00:00,,,,,,,,,,,,,,,,,,,,,,,,,,,,,0.15,ResultDailyTotal,"AMOUNT=0.15, CONCENTRATION=null",9801773184,51920003,97,Paradigm 515
/06,23:33:28,8/31/06 23:33:28,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9801773187,51920003,100,Paradigm 515
/06,23:33:54,8/31/06 23:33:54,,,,,,,,,,,Fixed,0.5,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.5, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.5, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9801773186,51920003,99,Paradigm 515
/06,23:34:28,8/31/06 23:34:28,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9801773185,51920003,98,Paradigm 515
06,00:12:41,9/1/06 00:12:41,,,,,,,,,,,Fixed,0.3,,,,,,,,,,,,,,,,,,Prime,"AMOUNT=0.3, CONCENTRATION=null, PROGRAMMED_AMOUNT=0.3, PRIME_TYPE=fixed, ACTION_REQUESTOR=pump",9801773183,51920003,96,Paradigm 515
06,00:44:29,9/1/06 00:44:29,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CurrentTimeDisplayFormat,FORMAT=d12,9801773087,51920003,0,Paradigm 515


```

#### RECORD 3 Prime 2006-10-04T08:11:30 head[5], body[0] 0x03
    op hex (5)
    0000   0x03 0x00 0x03 0x00 0x03                   .....
    decimal
              3    0    3    0    3
    datetime (2006-10-04T08:11:30)
    0000   0x9e 0x8b 0x08 0x04 0x06                   .....
    body (0)

date 2006-10-04
10 = 0x0a
4  = 0x04

#### RECORD 4 ResultTotals MIDNIGHT!? head[2], body[38] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x03 0x30 0xa4 0x06                   ..0..
    body (38)
    hex
    0000   0x6c 0xa4 0x06 0x05 0x0c 0x00 0xe8 0x00    l.......
    0008   0x00 0x00 0x00 0x03 0x30 0x03 0x30 0x64    ....0.0d
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
            108  164    6    5   12    0  232    0
              0    0    0    3   48    3   48  100
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0

```
date 2006-10-04
10 = 0x0a
4  = 0x04
5  = 0x05
body[2] = 0xa4 = ( 0x0a << 4 ) | ( 0x04 )
```

#### RECORD 5 ResultTotals MIDNIGHT!? head[2], body[38] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x03 0x36 0xa5 0x06                   ..6..
    body (38)
    hex
    0000   0x6c 0xa5 0x06 0x05 0x0c 0x00 0xe8 0x00    l.......
    0008   0x00 0x00 0x00 0x03 0x36 0x03 0x36 0x64    ....6.6d
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
            108  165    6    5   12    0  232    0
              0    0    0    3   54    3   54  100
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0

```
date 2006-10-05
10 = 0x0a
4  = 0x04
5  = 0x05
body[2] = 0xa5 = ( 0x0a << 4 ) | ( 0x05 )
```

#### RECORD 6 ResultTotals MIDNIGHT!? head[2], body[38] 0x07
    op hex (2)
    0000   0x07 0x00                                  ..
    decimal
              7    0
    datetime (MIDNIGHT!?)
    0000   0x00 0x03 0x36 0xa6 0x06                   ..6..
    body (38)
    hex
    0000   0x6c 0xa6 0x06 0x05 0x0c 0x00 0xe8 0x00    l.......
    0008   0x00 0x00 0x00 0x03 0x36 0x03 0x36 0x64    ....6.6d
    0010   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0018   0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00    ........
    0020   0x00 0x00 0x00 0x00 0x00 0x00              ......
    decimal
            108  166    6    5   12    0  232    0
              0    0    0    3   54    3   54  100
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0    0    0
              0    0    0    0    0    0

```
date 2006-10-06
month = 10 = 0x0a
5          = 0x05
day = 6    = 0x06
body[2]    = 0xa6 = ( 0x0a << 4 ) | ( 0x06 )
```

#### RECORD 7 Record 2006-10-07T23:01:00 head[2], body[0] 0x19
    op hex (2)
    0000   0x19 0x00                                  ..
    decimal
             25    0
    datetime (2006-10-07T23:01:00)
    0000   0x80 0x81 0x17 0x07 0x06                   .....
    body (0)





