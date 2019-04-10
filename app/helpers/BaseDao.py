from app import db
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class BaseDao:

  def __init__(self, tableName, modelClass):
    self._tableName = tableName
    self._mapper = SQLMapper(tableName, modelClass)
  
  def getAll(self):
    query = 'SELECT * FROM {}'.format(self._tableName)
    results = db.select(query)
    return self._mapper.from_tuples(results)

  def getById(self, id):
    query = 'SELECT * FROM {} WHERE id = {}'.format(self._tableName, id)
    result = db.select(query, limit=1)
    if result:
      return self._mapper.from_tuple(result)
    else:
      raise NotFoundException("No {} found with id '{:d}'".format(self._tableName, id))

  def save(self, data):
    raise NotImplementedError()

  def replace(self, id, data):
    raise NotImplementedError()

  def delete(self, id):
    raise NotImplementedError()
