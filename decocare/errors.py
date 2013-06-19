
class StickError(Exception): pass

class AckError(StickError): pass

class BadDeviceCommError(AckError): pass

#####
# EOF
