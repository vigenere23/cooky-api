import unittest
from src.infra.db.refactor.mysql_condition_builder import MysqlConditionBuilder
from unittest import TestCase

class MysqlConditionBuilderTest(TestCase):

    def test_query(self):
        condition = MysqlConditionBuilder().where(
            ['Comment.id = %(id_Comment)s', 'Recipe.name LIKE %(name)s'], data={'id_Comment': 123, 'name': 'lolo'}
        ).where(
            ['Recipe.type = ITALIAN'], data={'rating': 0}
        ).where(
            []
        ).build()

        query = condition.query()
        data = condition.data()

        expected_query = 'WHERE (Comment.id = %(id_Comment)s AND Recipe.name LIKE %(name)s) OR (Recipe.type = ITALIAN)'
        expected_data = {'id_Comment': 123, 'name': 'lolo', 'rating': 0}

        self.assertEqual(query, expected_query)
        self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()
