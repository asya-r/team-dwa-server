import requests
import json

url = 'http://localhost:5000/registration'
myobj = {'first_name': 'somevalue', 'last_name': 'sds', 'email': 'ssdss', 'password': 'sdss'}

#x = requests.post(url, json=myobj)
x = requests.post('http://localhost:5000/show_person', json={'id': 2})
print(x.content)