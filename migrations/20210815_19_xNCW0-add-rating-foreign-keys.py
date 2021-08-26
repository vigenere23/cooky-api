"""
Add Rating foreign keys
"""

from yoyo import step

__depends__ = {'20210815_18_l2Evg-add-ingredient-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
        ADD CONSTRAINT Rating_Recipe_FK
            FOREIGN KEY (id_Recipe) REFERENCES Recipe(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
        ADD CONSTRAINT Rating_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
        DROP CONSTRAINT Rating_Recipe_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
        DROP CONSTRAINT Rating_User_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2)
]
