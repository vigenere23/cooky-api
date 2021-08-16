"""
Add NewCartAfterCommand trigger
"""

from yoyo import step

__depends__ = {'20210815_33_EUtEk-add-updatereciperatingonratingupdate-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER NewCartAfterCommand
        AFTER INSERT ON Command
        FOR EACH ROW
        BEGIN
            SET @userId := (SELECT Cart.id_User FROM Cart WHERE Cart.id = NEW.id_Cart);
            INSERT INTO Cart (id, id_User, totalCost)
            VALUES (NULL, @userId, 0);
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS NewCartAfterCommand;
    """)

steps = [
    step(apply, rollback)
]
