
from decocare import commands
import types

class Task (object):
  def __init__ (self, msg, **kwargs):
    self.msg = msg
    pass
  def __get__ (self, obj, objtype=None):
    if obj is None:
      return self
    else:
      return types.MethodType(self, obj)
  def __call__ (self, inst):
    return inst.session.query(self.msg).getData( )

class PumpModel (object):
  bolus_strokes = 20
  basal_strokes = 40
  def __init__(self, model, session):
    self.model = model
    self.session = session

  read_status = Task(commands.ReadPumpStatus)
  read_temp_basal = Task(commands.ReadBasalTemp)
  read_settings = Task(commands.ReadSettings)
  read_reservoir = Task(commands.ReadRemainingInsulin)

class Model508 (PumpModel):
  pass

class Model511 (Model508):
  pass

class Model512 (Model511):
  pass

class Model515 (Model512):
  pass

class Model522 (Model515):
  pass

class Model523 (Model522):
  pass

class Model530 (Model523):
  pass

class Model540 (Model530):
  pass

class Model554 (Model540):
  pass

known = {
  '508': Model508
, '511': Model511
, '512': Model512
, '515': Model515
, '522': Model522
, '523': Model523
, '530': Model530
, '540': Model540
, '554': Model554
}

def lookup (model, session):
  klass = known.get(model, PumpModel)
  return klass(model, session)

