"""
Add UpdateSubCostCartItemOnUpdate trigger
"""

from yoyo import step

__depends__ = {'20210815_34_OAxfw-add-newcartaftercommand-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TRIGGER UpdateSubCostCartItemOnUpdate
        BEFORE UPDATE ON CartItem
        FOR EACH ROW
        BEGIN
            SET @baseCost := (SELECT I.baseCost FROM Ingredient I WHERE I.id = NEW.id_Ingredient);
            SET NEW.subCost := @baseCost * NEW.multiplier;
        END;
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TRIGGER IF EXISTS UpdateSubCostCartItemOnUpdate;
    """)

steps = [
    step(apply, rollback)
]
