import requests

get_responce=requests.get('http://127.0.0.1:8000/api/',json={'title':'jasur','discount':10.2,'price':120})
print('------>',get_responce.json()) 