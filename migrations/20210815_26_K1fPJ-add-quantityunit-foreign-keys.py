"""
Add QuantityUnit foreign keys
"""

from yoyo import step

__depends__ = {'20210815_25_KoC3J-add-command-foreign-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE QuantityUnit
        ADD CONSTRAINT QuantityUnit_QuantityType_FK
            FOREIGN KEY (id_QuantityType) REFERENCES QuantityType(id);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE QuantityUnit
        DROP CONSTRAINT QuantityUnit_QuantityType_FK;
    """)

steps = [
    step(apply, rollback)
]
