"""
Add LikeRecipe foreign keys
"""

from yoyo import step

__depends__ = {'20210815_22_NRaLn-add-recipeingredient-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
        ADD CONSTRAINT LikeRecipe_Recipe_FK
            FOREIGN KEY (id_Recipe) REFERENCES Recipe(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
        ADD CONSTRAINT LikeRecipe_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
        DROP CONSTRAINT LikeRecipe_Recipe_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE LikeRecipe
        DROP CONSTRAINT LikeRecipe_User_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2)
]
