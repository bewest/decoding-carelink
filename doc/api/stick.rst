.. _stick:

=====
Stick
=====

This manages communications with the usb stick itself.
This is really the heart of the whole package.

Given a :ref:`link`, with read/write methods, this module will allow
using the usb stick as a radio to communicate with compatible medical
devices.

:mod:`stick` Module
-------------------

.. automodule:: decocare.stick
    :members:
    :undoc-members:
    :show-inheritance:

The carelink usb stick acts like a modem.
It responds to modem commands, in order to exchange data with a remote
end-point.  In this case, our little carelink usb modem responds to a
variety of binary commands, which you must use in a co-ordinated flow
to exchange data with the remote equipment.  Also, in our case, the
only remote equipment the carelink usb stick is known to talk to are
the Me**ronic Par**igm series pumps.

The purpose of this module is to encapsulate the low level operations
needed to use the stick in any practical sense.  It serves as a
set of guides and tutorials which should help people trying to
understand or their therapy better.  This module seems mostly correct,
but things start to fall apart when downloading lots of data.  The
protocol is either sensitive to some timing somewhere that I'm
unaware of, or when CRC errors or other things happen, I simply do the
wrong thing to recover.

Please ask Medtronic for more information on how to learn what your
device is doing.


