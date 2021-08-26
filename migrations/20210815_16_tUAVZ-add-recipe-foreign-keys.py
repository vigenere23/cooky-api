"""
Add Recipe foreign keys
"""

from yoyo import step

__depends__ = {'20210815_15_gVpn2-create-table-quantitytype'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Recipe
        ADD CONSTRAINT Recipe_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Recipe
        DROP CONSTRAINT Recipe_User_FK;
    """)

steps = [
    step(apply, rollback)
]
