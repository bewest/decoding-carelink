
# What do prime events look like?

```
0th byte - prime event ( **0x03** )
1th byte - prime type (0, fixed vs 1, manual !?!?)
2th byte - programmed amount (or 0 == manual!??)
3th byte - concentration???
4th byte - amount primed
5th byte - seconds + (0x40) !?
6th byte - minutes + (0xC0) !?
7th byte - hours (24 hour)
8th byte - EOF?
9th byte - EOF?

```

### priming-records/fixed-4-49.hex
```0x03 0x00 0x03 0x00 0x03 0x4c 0xf1 0x10 0x07 0x06```

### priming-records/fixed-5-10.hex
```0x03 0x00 0x03 0x00 0x03 0x66 0xca 0x11 0x07 0x06```

### priming-records/fixed-5:28.hex
```0x03 0x00 0x03 0x00 0x03 0x73 0xdc 0x11 0x07 0x06```

### priming-records/fixed-5-41.hex
```0x03 0x00 0x03 0x00 0x03 0x4e 0xe9 0x11 0x07 0x06```

### priming-records/fixed-5-57.hex
```0x03 0x00 0x03 0x00 0x03 0x42 0xf9 0x11 0x07 0x06```

### priming-records/fixed-6-02.hex
```0x03 0x00 0x03 0x00 0x03 0x45 0xc2 0x12 0x07 0x06```

### priming-records/manual-4-49.hex
```0x03 0x00 0x00 0x00 0x13 0x74 0xf0 0x30 0x07 0x06```

### Rewind Events?

Same thing, but no parameters:

```
0th byte - rewind event ( **0x21** )
1th byte - NULL?
2th byte - seconds + (0x40) !?
3th byte - minutes + (0xC0) !?
4th byte - hours (24 hour)
5th byte - EOF?
6th byte - EOF?
```

### Time of Day

We believe all events encode time of day this way:
EG:
```
17:28:51 -> 0x73 0xDC 0x11
```

* hours `0x11` -> `decimal 17`, ie 5pm.
* minutes `0xDC - 0x40` = `28 decimal`
* seconds `0x73 - 0xC0` = `51 decimal`

We believe the `0x40` and or `0xC0` may be used to indicate the
**action requestor**, either being the PUMP or RF, or TBD as hinted by
Carelink CSV exports.

It turns out that the seconds and minutes and hours are the first
bytes in the in basically every record.  The "midnight" sentinel
record may be an exception.

