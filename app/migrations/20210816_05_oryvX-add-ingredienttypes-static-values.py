"""
Add IngredientTypes static values
"""

from yoyo import step

__depends__ = {'20210816_04_czm9U-add-cascaderecipedelete-trigger'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO IngredientType (id,name) VALUES
            (NULL, 'Dairy products'),
            (NULL, 'Oils'),
            (NULL, 'Fruits and vegetables'),
            (NULL, 'Confectionery'),
            (NULL, 'Cereal products'),
            (NULL, 'Meat products'),
            (NULL, 'Fish products'),
            (NULL, 'Egg products'),
            (NULL, 'Spices'),
            (NULL, 'Beverages'),
            (NULL, 'Salads'),
            (NULL, 'Prepared foods'),
            (NULL, 'Others');
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM IngredientType WHERE id IN (1,2,3,4,5,6,7,8,9,10,11,12,13);
    """)

steps = [
    step(apply, rollback)
]
