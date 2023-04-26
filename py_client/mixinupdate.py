import requests

endpoint=requests.post('http://127.0.0.1:8000/updatemixin/1/',
                       json={'title':'python10000','discount':40.2,'price':10})
print('--post',endpoint.json)