

class PumpModel (object):
  bolus_strokes = 20
  basal_strokes = 40
  def __init__(self, model):
    self.model = model

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

def lookup (model):
  klass = known.get(model, PumpModel)
  return klass(model)

