import requests
from getpass import getpass

password=getpass('What is your password? ')
username=input('What is your username? ')
auth_token_endpoint=requests.post('http://127.0.0.1:8000/auth/',json={'username':username,'password':password})




if auth_token_endpoint.status_code==200:
    token=auth_token_endpoint.json()['token']
    headers={'Authorization':f'Bearer {token}'}
endpoint=requests.get('http://127.0.0.1:8000/api/product/2/',headers=headers)
print('--------get',endpoint.json()) 