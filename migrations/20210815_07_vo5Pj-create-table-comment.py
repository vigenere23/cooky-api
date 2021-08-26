"""
Create table Comment
"""

from yoyo import step

__depends__ = {'20210815_06_5C2ui-create-table-rating'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Comment (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Recipe INTEGER NOT NULL,
            id_User INTEGER NULL DEFAULT NULL,
            text MEDIUMTEXT NULL DEFAULT NULL,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Comment;
    """)

steps = [
    step(apply, rollback)
]
