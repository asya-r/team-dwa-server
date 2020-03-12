from peewee import *

db = MySQLDatabase('teamdwa', user='teamdwa', password='321', host='localhost', port=3306)


class Person(Model):
    first_name = CharField()
    last_name = CharField()
    patronymic = CharField(null=True)
    email = CharField(unique=True)
    phone = DecimalField(null=True)
    password = CharField()

    class Meta:
        database = db


if __name__ == '__main__':
    db.connect()
    db.create_tables([Person])