"""
Create table Cart
"""

from yoyo import step

__depends__ = {'20210815_03_uKjhB-create-table-recipe'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Cart (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_User INTEGER NOT NULL,
            totalCost FLOAT(16,2) NOT NULL DEFAULT 0,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Cart;
    """)

steps = [
    step(apply, rollback)
]
