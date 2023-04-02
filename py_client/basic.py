import requests

get_responce=requests.post('http://127.0.0.1:8000/api/',json={'title':'fayzulloh','discount':10.2,'price':120})
print('------>',get_responce.json()) 