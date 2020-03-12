import requests
import json

url = 'http://localhost:5000/registration'
myobj = {'first_name': 'somevalue', 'last_name': 'sds', 'email': 'ssss', 'password': 'sdss'}

x = requests.post(url, data=myobj)