"""
Add CartItem foreign keys
"""

from yoyo import step

__depends__ = {'20210815_20_Bm4bx-add-comment-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
        ADD CONSTRAINT CartItem_Ingredient_FK
            FOREIGN KEY (id_Ingredient) REFERENCES Ingredient(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
        ADD CONSTRAINT CartItem_Cart_FK
            FOREIGN KEY (id_Cart) REFERENCES Cart(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
        DROP CONSTRAINT CartItem_Ingredient_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE CartItem
        DROP CONSTRAINT CartItem_Cart_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2)
]
