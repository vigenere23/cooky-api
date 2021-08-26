"""
Add QuantityType static values
"""

from yoyo import step

__depends__ = {'20210816_05_oryvX-add-ingredienttypes-static-values'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO QuantityType (id,name) VALUES
            (NULL, 'Volume'),
            (NULL, 'Weight'),
            (NULL, 'Unit');
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM QuantityType WHERE id IN (1,2,3);
    """)

steps = [
    step(apply, rollback)
]
