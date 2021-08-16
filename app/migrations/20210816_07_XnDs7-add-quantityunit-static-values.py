"""
Add QuantityUnit static values
"""

from yoyo import step

__depends__ = {'20210816_06_EmbYd-add-quantitytype-static-values'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO QuantityUnit (id,id_QuantityType,name,abbreviation) VALUES
            (NULL, 1, 'teaspoon', 'tsp'),
            (NULL, 1, 'tablespoon', 'tbsp'),
            (NULL, 1, 'fluid ounce', 'fl oz'),
            (NULL, 1, 'cup', 'cup'),
            (NULL, 1, 'milliliter', 'mL'),
            (NULL, 1, 'liter', 'L'),
            (NULL, 1, 'deciliter', 'dL'),
            (NULL, 2, 'pound', 'lb'),
            (NULL, 2, 'ounce', 'oz'),
            (NULL, 2, 'miligram', 'mg'),
            (NULL, 2, 'gram', 'g'),
            (NULL, 2, 'kilogram', 'kg'),
            (NULL, 3, 'unit', 'unit');
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM QuantityUnit WHERE id IN (1,2,3,4,5,6,7,8,9,10,11,12,13);
    """)

steps = [
    step(apply, rollback)
]
