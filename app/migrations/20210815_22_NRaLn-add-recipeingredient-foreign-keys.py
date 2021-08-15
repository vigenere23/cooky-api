"""
Add RecipeIngredient foreign keys
"""

from yoyo import step

__depends__ = {'20210815_21_snvCh-add-cartitem-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        ADD CONSTRAINT RecipeIngredient_Recipe_FK
            FOREIGN KEY (id_Recipe) REFERENCES Recipe(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        ADD CONSTRAINT RecipeIngredient_Ingredient_FK
            FOREIGN KEY (id_Ingredient) REFERENCES Ingredient(id);
    """)

def apply3(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        ADD CONSTRAINT RecipeIngredient_QuantityUnit_FK
            FOREIGN KEY (id_QuantityUnit) REFERENCES QuantityUnit(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        DROP CONSTRAINT RecipeIngredient_Recipe_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        DROP CONSTRAINT RecipeIngredient_Ingredient_FK;
    """)

def rollback3(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE RecipeIngredient
        DROP CONSTRAINT RecipeIngredient_QuantityUnit_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2),
    step(apply3, rollback3)
]
