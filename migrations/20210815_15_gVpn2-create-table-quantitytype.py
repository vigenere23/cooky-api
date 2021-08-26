"""
Create table QuantityType
"""

from yoyo import step

__depends__ = {'20210815_14_i3emq-create-table-quantityunit'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE QuantityType (
            id INTEGER NOT NULL AUTO_INCREMENT,
            name VARCHAR(20) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (name)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS QuantityType;
    """)

steps = [
    step(apply, rollback)
]
