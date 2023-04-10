import requests
data={
    'title':'xxxxxxxx',
    'price':101,
    'discount':10.1,
}

endpoint=requests.put('http://127.0.0.1:2000/api/update/1/',json=data)
print('update',endpoint.json)
