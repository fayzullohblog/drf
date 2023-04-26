import requests
from getpass import getpass

password=getpass()
auth_token_endpoint=requests.post('http://127.0.0.1:8000/auth/',json={'username':'cfe','password':password})




if auth_token_endpoint.status_code==200:
    token=auth_token_endpoint.json()['token']
    headers={'Authorization':f'Token {token}'}
endpoint=requests.get('http://127.0.0.1:8000/api/product/2/',headers=headers)
print('--------get',endpoint.json()) 