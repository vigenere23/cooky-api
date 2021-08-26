"""
Create table Recipe
"""

from yoyo import step

__depends__ = {'20210815_02_z3oJE-create-table-account'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Recipe (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_User INTEGER NOT NULL,
            name VARCHAR(50) NOT NULL,
            description MEDIUMTEXT NULL DEFAULT NULL,
            directives MEDIUMTEXT NOT NULL,
            rating FLOAT(8,2) NOT NULL DEFAULT 0.00,
            PRIMARY KEY (id),
            UNIQUE KEY (name)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Recipe;
    """)

steps = [
    step(apply, rollback)
]
