"""
Add LikeRecipe unique keys
"""

from yoyo import step

__depends__ = {'20210815_29_SXGbr-add-rating-unique-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
            ADD CONSTRAINT CartItem_id_Ingredient_id_Cart_UK
            UNIQUE (id_Ingredient, id_Cart);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
        DROP CONSTRAINT CartItem_id_Ingredient_id_Cart_UK;
    """)

steps = [
    step(apply, rollback)
]
