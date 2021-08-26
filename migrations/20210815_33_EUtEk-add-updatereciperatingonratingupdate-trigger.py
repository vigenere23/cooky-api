"""
Add UpdateRecipeRatingOnRatingUpdate trigger
"""

from yoyo import step

__depends__ = {'20210815_32_8zGYP-add-updatereciperatingonratinginsert-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateRecipeRatingOnRatingUpdate
        AFTER UPDATE ON Rating
        FOR EACH ROW
        BEGIN
            SET @rating := (SELECT AVG(R.value) FROM Rating R WHERE R.id_Recipe = NEW.id_Recipe);
            UPDATE Recipe R SET R.rating := @rating WHERE R.id = NEW.id_Recipe;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateRecipeRatingOnRatingUpdate;
    """)

steps = [
    step(apply, rollback)
]
