"""
Add UpdateTotalCostCartOnCartItemDelete trigger
"""

from yoyo import step

__depends__ = {'20210816_01_F2h2F-add-updatetotalcostcartoncartiteminsert-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateTotalCostCartOnCartItemDelete
        AFTER DELETE ON CartItem
        FOR EACH ROW
        BEGIN
            SET @totalCost := IFNULL((SELECT SUM(C.subCost) FROM CartItem C WHERE C.id_Cart = OLD.id_Cart), 0);
            UPDATE Cart C SET C.totalCost := @totalCost WHERE C.id = OLD.id_Cart;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateTotalCostCartOnCartItemDelete;
    """)

steps = [
    step(apply, rollback)
]
