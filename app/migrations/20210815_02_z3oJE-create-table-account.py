"""
Create table Account
"""

from yoyo import step

__depends__ = {'20210814_01_EX5ba-create-table-user'}

def apply(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE Account (
            id INTEGER NOT NULL AUTO_INCREMENT,
            id_User INTEGER NOT NULL,
            id_Address INTEGER NOT NULL,
            firstName VARCHAR(50) NOT NULL,
            lastName VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARBINARY(100) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY (id_User)
        );
    """)

def rollback(conn):
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Account;
    """)

steps = [
    step(apply, rollback)
]
