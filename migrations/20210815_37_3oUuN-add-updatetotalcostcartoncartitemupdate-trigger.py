"""
Add UpdateTotalCostCartOnCartItemUpdate trigger
"""

from yoyo import step

__depends__ = {'20210815_36_9KEVU-add-updatesubcostcartitemoninsert-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateTotalCostCartOnCartItemUpdate
        AFTER UPDATE ON CartItem
        FOR EACH ROW
        BEGIN
            SET @totalCost := (SELECT SUM(C.subCost) FROM CartItem C WHERE C.id_Cart = NEW.id_Cart);
            UPDATE Cart C SET C.totalCost := @totalCost WHERE C.id = NEW.id_Cart;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateTotalCostCartOnCartItemUpdate;
    """)

steps = [
    step(apply, rollback)
]
