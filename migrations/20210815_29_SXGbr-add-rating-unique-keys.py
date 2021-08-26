"""
Add Rating unique keys
"""

from yoyo import step

__depends__ = {'20210815_28_QrGSr-add-recipeingredient-unique-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
            ADD CONSTRAINT Rating_id_Recipe_id_User_UK
            UNIQUE (id_Recipe, id_User);
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        ALTER TABLE Rating
        DROP CONSTRAINT Rating_id_Recipe_id_User_UK;
    """)

steps = [
    step(apply, rollback)
]
