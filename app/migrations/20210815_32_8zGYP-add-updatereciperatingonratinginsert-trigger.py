"""
Add UpdateRecipeRatingOnRatingInsert trigger
"""

from yoyo import step

__depends__ = {'20210815_31_r06CY-add-newcartfornewuser-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateRecipeRatingOnRatingInsert
        AFTER INSERT ON Rating
        FOR EACH ROW
        BEGIN
            SET @rating := (SELECT AVG(R.value) FROM Rating R WHERE R.id_Recipe = NEW.id_Recipe);
            UPDATE Recipe R SET R.rating := @rating WHERE R.id = NEW.id_Recipe;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateRecipeRatingOnRatingInsert;
    """)

steps = [
    step(apply, rollback)
]
