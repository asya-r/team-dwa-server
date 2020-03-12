from flask import Flask, request
from DbModels import Person, Complaint
from db_connect import db_session_init
import json

db_session_init()
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/registration', methods=['POST'])
def registration():
    person = Person()
    print(request.get_data())
    content = request.get_json()
    for k in content.keys():
        print(k)
        setattr(person, k, content[k])
    person.save()
    return json.dumps({'id': person.id})


@app.route('/login', methods=['POST'])
def login():
    content = request.get_json()
    person = Person.select().where(Person.email == content['email'] and Person.password == content['password'])
    if person:
        return json.dumps({'id': person[0].id})
    return


@app.route('/send_claim', methods=['POST'])
def send_complaint():
    complaint = Complaint()
    content = request.get_json()
    for k in content.keys():
        print(k)
        setattr(complaint, k, content[k])
    complaint.save()
    return json.dumps({'id': complaint.id})


if __name__ == '__main__':
    app.run()