"""
Add CascadeRecipeDelete trigger
"""

from yoyo import step

__depends__ = {'20210816_03_HYHJE-add-preventupdateofcartitemifiscommand-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER CascadeRecipeDelete
        BEFORE DELETE ON Recipe
        FOR EACH ROW
        BEGIN
            DELETE FROM Comment WHERE Comment.id_Recipe = OLD.id;
            DELETE FROM Rating WHERE Rating.id_Recipe = OLD.id;
            DELETE FROM LikeRecipe WHERE LikeRecipe.id_Recipe = OLD.id;
            DELETE FROM RecipeIngredient WHERE RecipeIngredient.id_Recipe = OLD.id;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS CascadeRecipeDelete;
    """)

steps = [
    step(apply, rollback)
]
