import requests

json={'title':'kamaz'}

endpoint=requests.post('http://127.0.0.1:8000/',json=json)

print(endpoint.json())