"""
Create table Address
"""

from yoyo import step

__depends__ = {'20210815_12_BcFYA-create-table-ingredienttype'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Address (
            id INTEGER NOT NULL AUTO_INCREMENT,
            number INTEGER NOT NULL,
            apartment INTEGER NULL DEFAULT NULL,
            street VARCHAR(30) NOT NULL,
            city VARCHAR(30) NOT NULL,
            country VARCHAR(30) NOT NULL,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Address;
    """)

steps = [
    step(apply, rollback)
]
