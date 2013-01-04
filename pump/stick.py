
import lib
import logging

log = logging.getLogger( ).getChild(__name__)

class Stick(object):
  """
    The carelink usb stick acts like a buffer.

    It has a variety of commands providing synchronous IO, eg, you may
    generally perform a read immediately after writing to it, and expect a
    response.

    The commands operate on a local buffer used to facilitate exchanging
    messages over RF with the pump. RF communication with the pump
    happens asynchronously, requiring us to go through 3 separate
    phases for each message we'd like to exchange with the pumps:
      * SET COMMAND
      * POLL
      * DOWNLOAD

    Each command is usually only 3 bytes.

    A special command is 
  """
  link = None
  def __init__(self, link):
    self.link = link

#####
# EOF
