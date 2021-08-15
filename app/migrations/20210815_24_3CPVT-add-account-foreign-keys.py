"""
Add Account foreign keys
"""

from yoyo import step

__depends__ = {'20210815_23_jYDr5-add-likerecipe-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Account
        ADD CONSTRAINT Account_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Account
        ADD CONSTRAINT Account_Address_FK
            FOREIGN KEY (id_Address) REFERENCES Address(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Account
        DROP CONSTRAINT Account_User_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Account
        DROP CONSTRAINT Account_Address_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2)
]
