import requests

endpoint=requests.get('http://127.0.0.1:8000/listmixin/')
print('--->?',endpoint.json())