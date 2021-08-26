"""
Add PreventUpdateOfCartItemIfIsCommand trigger
"""

from yoyo import step

__depends__ = {'20210816_02_DBq4t-add-updatetotalcostcartoncartitemdelete-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER PreventUpdateOfCartItemIfIsCommand
        BEFORE UPDATE ON CartItem
        FOR EACH ROW
        BEGIN
            SET @commandCountWithCartId := (SELECT COUNT(*) FROM Command C WHERE C.id_Cart = NEW.id_Cart);
            IF @commandCountWithCartId > 0 THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = "Le panier à déjà été commandé et n'est plus modifiable";
            END IF;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS PreventUpdateOfCartItemIfIsCommand;
    """)

steps = [
    step(apply, rollback)
]
