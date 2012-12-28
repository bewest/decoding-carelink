
import lib

class USBProductInfo( object ):
  """Get product info from the usb device."""
  code   = [ 4 ]
  SW_VER = 16
  label  = 'usb.productInfo'
  rf_table  = { 001: '868.35Mhz' ,
                000: '916.5Mhz'  ,
                255: '916.5Mhz'  }
  iface_key = { 3: 'USB',
                1: 'Paradigm RF' }

  @classmethod
  def decodeInterfaces( klass, L ):
    n, tail    = L[ 0 ], L[ 1: ]
    interfaces = [ ]
    for x in xrange( n ):
      i    = x*2
      k, v = tail[i], tail[i+1]
      interfaces.append( ( k, klass.iface_key.get( v, 'UNKNOWN'  ) ) )
    return interfaces

  @classmethod
  def decode( klass,  data ):
    return {
      'rf.freq'          : klass.rf_table.get( data[ 5 ], 'UNKNOWN' )
    , 'serial'           : str( data[ 0:3 ]).encode( 'hex'  )
    , 'product.version'  : '{0}.{1}'.format( *data[ 3:5 ] )
    , 'description'      : str( data[ 06:16 ] )
    , 'software.version' : '{0}.{1}'.format( *data[ 16:18 ] )
    , 'interfaces'       : klass.decodeInterfaces( data[ 18: ] )
    }

class InterfaceStats( object ):
  code          = [ 5 ]
  INTERFACE_IDX = 19
  label         = 'usb.interfaceStats'
  @classmethod
  def decode( klass, data):
    return {
      'errors.crc'      : data[ 0 ]
    , 'errors.sequence' : data[ 1 ]
    , 'errors.naks'     : data[ 2 ]
    , 'errors.timeouts' : data[ 3 ]
    , 'packets.received': lib.BangLong( data[ 4: 8 ] )
    , 'packets.transmit': lib.BangLong( data[ 8:12 ] )
    }

if __name__ == '__main__':
  import doctest
  doctest.testmod( )
