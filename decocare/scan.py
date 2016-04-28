
import glob

class ID:
  VENDOR  = 0x0a21
  PRODUCT = 0x8001
  @classmethod
  def template (Klass, prefix):
    postfix = '*'
    usb_id = "%04x_%04x" % (ID.VENDOR, ID.PRODUCT)
    candidate = ''.join([prefix, usb_id, postfix])
    return candidate

def scan (prefix='/dev/serial/by-id/*-', template=ID.template):
  candidate = template(prefix)
  results = glob.glob(candidate)
  return (results[0:1] or ['']).pop( )

if __name__ == '__main__':
  candidate = scan( )
  print candidate

