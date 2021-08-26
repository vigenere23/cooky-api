"""
Add CartItem unique keys
"""

from yoyo import step

__depends__ = {'20210815_26_K1fPJ-add-quantityunit-foreign-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
            ADD CONSTRAINT LikeRecipe_id_Recipe_id_User_UK
            UNIQUE (id_Recipe, id_User);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
        DROP CONSTRAINT LikeRecipe_id_Recipe_id_User_UK;
    """)

steps = [
    step(apply, rollback)
]
