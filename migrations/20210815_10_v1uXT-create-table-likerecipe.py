"""
Create table LikeRecipe
"""

from yoyo import step

__depends__ = {'20210815_09_FoKuk-create-table-recipeingredient'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE LikeRecipe (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Recipe INTEGER NOT NULL,
            id_User INTEGER NOT NULL,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS LikeRecipe;
    """)

steps = [
    step(apply, rollback)
]
