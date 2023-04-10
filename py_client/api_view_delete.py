import requests

product_id=int(input('what is th product id you want see? '))

try:
    if product_id:
        endpoint=requests.delete(f'http://127.0.0.1:3000/api/delete/<int:{product_id}>/')
        print('-----1',endpoint)
        print(endpoint.json())
except:
    print(f'{product_id} not is valid id')
