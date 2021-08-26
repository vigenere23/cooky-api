"""
Add Comment foreign keys
"""

from yoyo import step

__depends__ = {'20210815_19_xNCW0-add-rating-foreign-keys'}

def apply1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Comment
        ADD CONSTRAINT Comment_Recipe_FK
            FOREIGN KEY (id_Recipe) REFERENCES Recipe(id);
    """)

def apply2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Comment
        ADD CONSTRAINT Comment_User_FK
            FOREIGN KEY (id_User) REFERENCES User(id);
    """)

def rollback1(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Comment
        DROP CONSTRAINT Comment_Recipe_FK;
    """)

def rollback2(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Comment
        DROP CONSTRAINT Comment_User_FK;
    """)

steps = [
    step(apply1, rollback1),
    step(apply2, rollback2),
]
