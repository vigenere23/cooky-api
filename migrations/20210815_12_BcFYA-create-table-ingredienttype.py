"""
Create table IngredientType
"""

from yoyo import step

__depends__ = {'20210815_11_bzY3P-create-table-command'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IngredientType (
            id INTEGER NOT NULL AUTO_INCREMENT,
            name VARCHAR(30) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (name)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS IngredientType;
    """)

steps = [
    step(apply, rollback)
]
