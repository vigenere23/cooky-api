"""
Add NewCartForNewUser trigger
"""

from yoyo import step

__depends__ = {'20210815_30_zX7xU-add-likerecipe-unique-keys'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER NewCartForNewUser
        AFTER INSERT ON User
        FOR EACH ROW
        BEGIN
            INSERT INTO Cart (id, id_User, totalCost)
            VALUES (NULL, NEW.id, 0);
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS NewCartForNewUser;
    """)

steps = [
    step(apply, rollback)
]
