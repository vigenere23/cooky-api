from app import db
from .model import CartItemModel
from app.helpers.BaseDao import BaseDao

class CartItemDao(BaseDao):

    def __init__(self):
        super().__init__('CartItem', CartItemModel)

    def getItemsByCart(self, id_Cart):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self._mapper.from_tuples(results)

    def getByCartAndIngredientIds(self, id_Cart, id_Ingredient):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        result = db.select(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient}, 1)
        return self._mapper.from_tuple(result)


    def deleteIngredient(self, id_Cart, id_Ingredient):
        query = 'DELETE FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        db.delete(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient})

    def modifyQuantity(self, multiplier, id_Cart, id_Ingredient):
        query = 'UPDATE CartItem SET multiplier = %(multiplier)s WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        db.replace(query, {'id_Cart': id_Cart, 'id_Ingredient': id_Ingredient, "multiplier": multiplier})
        return self.getByCartAndIngredientIds(id_Cart, id_Ingredient)
        
    def save(self, cartItemModel):
        if not isinstance(cartItemModel, CartItemModel):
            raise ValueError("cartItemModel should be of type CartItemModel")
        query = 'INSERT INTO CartItem (id, id_Ingredient, id_Cart, multiplier, subCost) VALUES (%s, %s, %s, %s, %s)'
        newItemId = db.insert(query, self._mapper.to_tuple(cartItemModel))
      
        if newItemId:
            return self.getById(newItemId)
        else:
            raise Exception("Could not save ingredient to cart")