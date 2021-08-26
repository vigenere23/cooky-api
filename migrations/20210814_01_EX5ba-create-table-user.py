"""
Create table User
"""

from yoyo import step

__depends__ = {}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE User (
            id INTEGER NOT NULL AUTO_INCREMENT,
            username VARCHAR(20) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (username)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS User;
    """)

steps = [
    step(apply, rollback)
]
