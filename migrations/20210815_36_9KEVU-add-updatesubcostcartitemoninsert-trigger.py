"""
Add UpdateSubCostCartItemOnInsert trigger
"""

from yoyo import step

__depends__ = {'20210815_35_GLmJX-add-updatesubcostcartitemonupdate-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateSubCostCartItemOnInsert
        BEFORE INSERT ON CartItem
        FOR EACH ROW
        BEGIN
            SET @baseCost := (SELECT I.baseCost FROM Ingredient I WHERE I.id = NEW.id_Ingredient);
            SET NEW.subCost := @baseCost * NEW.multiplier;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateSubCostCartItemOnInsert;
    """)

steps = [
    step(apply, rollback)
]
