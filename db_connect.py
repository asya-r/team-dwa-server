from pymysql import connect
from peewee import MySQLDatabase


class DbSchema(object):
    _create = 'CREATE SCHEMA {} CHARACTER SET {} COLLATE {};'
    _drop = 'DROP SCHEMA IF EXISTS {};'
    _exist = 'SELECT SCHEMA_NAME FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "{}";'

    def __init__(self, name, charset='utf8mb4', collate='utf8mb4_unicode_ci'):
        self._name = name
        self._charset = charset
        self._collate = collate

    @property
    def create_query(self):
        return self._create.format(
            self._name,
            self._charset,
            self._collate
        )

    @property
    def drop_query(self):
        return self._drop.format(self._name)

    @property
    def is_exist_query(self):
        return self._exist.format(self._name)


class CustomMySQLDatabase(MySQLDatabase):
    @staticmethod
    def _check_schema(database, host, user, password):
        schema = DbSchema(database)
        conn = connect(
            host=host,
            user=user,
            password=password,
            charset='utf8mb4'
        )
        with conn.cursor() as cursor:
            cursor.execute(schema.is_exist_query)
            if not cursor.rowcount:
                cursor.execute(schema.create_query)
        conn.commit()
        conn.close()

    def init(self, database, **kwargs):
        if database:
            self._check_schema(database, kwargs['host'], kwargs['user'], kwargs['password'])
        super(CustomMySQLDatabase, self).init(database, **kwargs)


db = CustomMySQLDatabase(None)


def db_session_init():
    db.init('teamdwa', user='teamdwa', password='321', host='localhost', port=3306)


db_session_init()
