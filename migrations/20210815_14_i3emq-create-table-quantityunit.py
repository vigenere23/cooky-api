"""
Create table QuantityUnit
"""

from yoyo import step

__depends__ = {'20210815_13_kB2oG-create-table-address'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE QuantityUnit (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_QuantityType INTEGER NOT NULL,
            name VARCHAR(20) NOT NULL,
            abbreviation VARCHAR(10) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (name, abbreviation)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS QuantityUnit;
    """)

steps = [
    step(apply, rollback)
]
