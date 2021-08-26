"""
Add UpdateTotalCostCartOnCartItemInsert trigger
"""

from yoyo import step

__depends__ = {'20210815_37_3oUuN-add-updatetotalcostcartoncartitemupdate-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateTotalCostCartOnCartItemInsert
        AFTER INSERT ON CartItem
        FOR EACH ROW
        BEGIN
            SET @totalCost := (SELECT SUM(C.subCost) FROM CartItem C WHERE C.id_Cart = NEW.id_Cart);
            UPDATE Cart C SET C.totalCost := @totalCost WHERE C.id = NEW.id_Cart;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateTotalCostCartOnCartItemInsert;
    """)

steps = [
    step(apply, rollback)
]
