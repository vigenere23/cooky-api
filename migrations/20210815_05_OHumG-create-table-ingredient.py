"""
Create table Ingredient
"""

from yoyo import step

__depends__ = {'20210815_04_ssEFI-create-table-cart'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Ingredient (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_IngredientType INTEGER NOT NULL,
            id_QuantityUnit INTEGER NOT NULL,
            name VARCHAR(30) NOT NULL,
            baseCost FLOAT(16,2) NOT NULL,
            baseQuantity INTEGER NOT NULL DEFAULT 1,
            PRIMARY KEY (id),
            UNIQUE KEY (name)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Ingredient;
    """)

steps = [
    step(apply, rollback)
]
