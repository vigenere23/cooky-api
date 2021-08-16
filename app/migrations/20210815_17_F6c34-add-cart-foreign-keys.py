"""
Add Cart foreign keys
"""

from yoyo import step

__depends__ = {'20210815_16_tUAVZ-add-recipe-foreign-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Cart
        ADD CONSTRAINT Cart_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Cart
        DROP CONSTRAINT Cart_User_FK;
    """)

steps = [
    step(apply, rollback)
]
