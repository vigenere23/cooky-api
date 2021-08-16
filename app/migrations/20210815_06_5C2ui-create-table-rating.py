"""
Create table Rating
"""

from yoyo import step

__depends__ = {'20210815_05_OHumG-create-table-ingredient'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Rating (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Recipe INTEGER NOT NULL,
            id_User INTEGER NOT NULL,
            value INTEGER NOT NULL,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Rating;
    """)

steps = [
    step(apply, rollback)
]
