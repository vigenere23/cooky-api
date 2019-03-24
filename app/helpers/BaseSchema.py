from app.helpers import queries

class BaseSchema:
  def __init__(self, table_name, modelClass):
    self.table_name = table_name
    self.column_names = []
    self.modelClass = modelClass

    column_infos = queries.getColumns(self.table_name)
    for column_info in column_infos:
      self.column_names.append(column_info[0])

  def from_tuples(self, SQLtuples):
    models = []
    for SQLtuple in SQLtuples:
      models.append(self.from_tuple(SQLtuple))
    return models

  def from_tuple(self, SQLtuple):
    model = {}
    for (i, value) in enumerate(SQLtuple):
      model[self.column_names[i]] = value
    return self.modelClass(**model)

  def from_data(self, data):
    model = {}
    for (key, value) in data.items():
      if key in self.column_names:
        model.__setattr__(key, value)
      else:
        raise AttributeError("Attribute {} does not exist for Table {}".format(key, self.table_name))
    return self.modelClass(model)

  def to_tuple(self):
    values = []
    for column_name in self.column_names:
      values.append(self[column_name])
    
    return tuple(values)
