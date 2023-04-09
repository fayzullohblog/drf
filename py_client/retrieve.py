import requests

endpoint=requests.get('http://127.0.0.1:8000/api/product/3/')
print(endpoint.json())