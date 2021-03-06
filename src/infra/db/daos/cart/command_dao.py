from src.context import db
from src.infra.db.models.cart import CommandModel
from src.infra.db.daos import BaseDao


class CommandDao(BaseDao):

    def __init__(self):
        super().__init__('Command', CommandModel)

    def getUserCommands(self, id_User):
        query = 'SELECT C.id, C.id_Cart, C.creationDate, C.arrivalDate FROM Command C, Cart WHERE Cart.id = C.id_Cart AND Cart.id_User = %(id_User)s'
        results = db.findAll(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)

    def save(self, commandsModel):
        if not isinstance(commandsModel, CommandModel):
            raise ValueError("commandsModel should be of type CommandModel")

        query = 'INSERT INTO Command (id, id_Cart, creationDate, arrivalDate) VALUES (%s, %s, %s, %s)'
        newCommand = db.create(query, self._mapper.to_tuple(commandsModel))

        if newCommand:
            return self.getById(newCommand)
        else:
            raise Exception("Could not add newCommand")
