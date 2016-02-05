
class StickError(Exception): pass

class AckError(StickError): pass

class BadDeviceCommError(AckError): pass

class DataTransferCorruptionError(Exception): pass

#####
# EOF
