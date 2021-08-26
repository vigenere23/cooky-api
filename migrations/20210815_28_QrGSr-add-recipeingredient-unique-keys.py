"""
Add RecipeIngredient unique keys
"""

from yoyo import step

__depends__ = {'20210815_27_HnYo4-add-cartitem-unique-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
            ADD CONSTRAINT RecipeIngredient_id_Recipe_id_Ingredient_UK
            UNIQUE (id_Recipe, id_Ingredient);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        DROP CONSTRAINT RecipeIngredient_id_Recipe_id_Ingredient_UK;
    """)

steps = [
    step(apply, rollback)
]
