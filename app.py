from flask import Flask, request
from DbModels import Person
from db_connect import db_session_init
import json

db_session_init()
from peewee import MySQLDatabase
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/registration', methods=['POST'])
def registration():
    person = Person()
    for k in request.form.keys():
        setattr(person, k, request.form[k])
    person.save()
    return str(person.id)


@app.route('/login', methods=['POST', 'GET'])
def login():
    person = Person.select().where(Person.email == request.form['email'] and Person.password == request.form['password'])
    if person:
        return str(person.id)
    return


@app.route('/send_claim', methods=['POST'])
def send_claim():
    pass


if __name__ == '__main__':
    app.run()