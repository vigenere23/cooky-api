from app.helpers.BaseModel import BaseModel

class CommandsModel(BaseModel):
  def __init__(self, id=None, id_Cart=None, creationDate=None, arrivalDate=None):
    self.id = id
    self.id_Cart = id_Cart
    self.creationDate = creationDate
    self.arrivalDate = arrivalDate