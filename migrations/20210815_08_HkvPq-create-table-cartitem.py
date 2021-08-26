"""
Create table CartItem
"""

from yoyo import step

__depends__ = {'20210815_07_vo5Pj-create-table-comment'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE CartItem (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_Ingredient INTEGER NOT NULL,
            id_Cart INTEGER NOT NULL,
            multiplier INT NOT NULL DEFAULT 1,
            subCost FLOAT(16,2) NOT NULL DEFAULT 0,
            PRIMARY KEY (id)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS CartItem;
    """)

steps = [
    step(apply, rollback)
]
