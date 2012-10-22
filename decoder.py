#!/usr/bin/python
"""
decoder.py - An analysis of Medtronic Carelink Diabetes protocol using
scapy.
"""

# stdlib
import user
import sys
import argparse
import logging
import binascii

logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('decoder')
logger.setLevel(logging.DEBUG)

# Requires scapy to be in your PYATHONPATH
#import scapy
from scapy.all import *
from scapy import utils

_usb_response = { 0x00: '', 'U': "Success", 'f': "Fail" }

class USBReq(Packet):
  name = "USBRequest"

  fields_desc = [
    XByteField("code", 0),
    ByteEnumField("resp", 0x00, _usb_response),
    XByteField("error", 0),
  ]

class Decoder(object):
  def __init__(self, path, opts):
    self.path = path
    self.opts = opts

  def __call__(self):
    self.open( )
    self.decode( )
    self.close( )

  def open(self):
    self.handle = None
    if self.path == '-':
      self.handle = sys.stdin
    else:
      self.handle = open(self.path, 'rU')

  def close(self):
    if self.path != '-':
      self.handle.close( )

  def decode(self):
    for line in self.handle.readlines( ):
      line = line.strip( )
      method, data = line.split(',')
      data = binascii.unhexlify(data)
      if method == 'out':
        print method
        p = USBReq(data)
        print p.show( )



class Console:
  _log_map = { 0: logging.ERROR, 1: logging.WARN,
               2: logging.INFO, 3: logging.DEBUG }
  def __init__(self, args):
    self.raw_args = args
    self.parser = self.get_argparser( )
    args = list(args)
    cmd, args = args[0], args[1:]
    self.opts = self.parser.parse_args((args))
    logger.setLevel(self._log_map.get(self.opts.verbose, 3))
    cmdverbose = ''
    if self.opts.verbose > 0:
      cmdverbose = '-' + ('v' * self.opts.verbose)
      
    #logger.info('opts: %s' % (pformat(args)))
    cmdline = [ cmd, cmdverbose ] + self.opts.input
    print ' '.join(cmdline)

  def main(self):
    logger.info('opening %s' % (self.opts.input))

    for item in self.opts.input:
      self.do_input(item)

  def do_input(self, item):
    decode = Decoder(item, self.opts)
    print decode( )

  def get_argparser(self):
    """Prepare an argument parser."""
    parser = argparse.ArgumentParser(description=__doc__ )
    parser.add_argument('-v', '--verbose', action='count', default=0,
                        help="Verbosity.")
    parser.add_argument('input', nargs='+', help="Input files")
    return parser

if __name__ == '__main__':
  app = Console(sys.argv)
  app.main( )

#####
# EOF
