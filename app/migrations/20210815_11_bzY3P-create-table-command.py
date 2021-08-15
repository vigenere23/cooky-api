"""
Create table Command
"""

from yoyo import step

__depends__ = {'20210815_10_v1uXT-create-table-likerecipe'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Command (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Cart INTEGER NOT NULL,
            creationDate DATETIME NOT NULL,
            arrivalDate DATETIME NULL DEFAULT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (id_Cart)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Command;
    """)

steps = [
    step(apply, rollback)
]
