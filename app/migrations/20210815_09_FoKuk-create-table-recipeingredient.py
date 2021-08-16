"""
Create table RecipeIngredient
"""

from yoyo import step

__depends__ = {'20210815_08_HkvPq-create-table-cartitem'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE RecipeIngredient (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Recipe INTEGER NOT NULL,
            id_Ingredient INTEGER NOT NULL,
            id_QuantityUnit INTEGER NOT NULL,
            totalQuantity INTEGER NOT NULL DEFAULT 1,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS RecipeIngredient;
    """)

steps = [
    step(apply, rollback)
]
