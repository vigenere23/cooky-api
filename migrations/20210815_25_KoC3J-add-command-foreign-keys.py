"""
Add Command foreign keys
"""

from yoyo import step

__depends__ = {'20210815_24_3CPVT-add-account-foreign-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Command
        ADD CONSTRAINT Command_Cart_FK
            FOREIGN KEY (id_Cart) REFERENCES Cart(id);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Command
        DROP CONSTRAINT Command_Cart_FK;
    """)

steps = [
    step(apply, rollback)
]
