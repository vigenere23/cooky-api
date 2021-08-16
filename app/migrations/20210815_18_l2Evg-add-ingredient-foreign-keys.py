"""
Add Ingredient foreign keys
"""

from yoyo import step

__depends__ = {'20210815_17_F6c34-add-cart-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Ingredient
        ADD CONSTRAINT Ingredient_IngredientType_FK
            FOREIGN KEY (id_IngredientType) REFERENCES IngredientType(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Ingredient
        ADD CONSTRAINT Ingredient_QuantityUnit_FK
            FOREIGN KEY (id_QuantityUnit) REFERENCES QuantityUnit(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Ingredient
        DROP CONSTRAINT Ingredient_IngredientType_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Ingredient
        DROP CONSTRAINT Ingredient_QuantityUnit_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2),
]
