import os
import requests

BASE_URL = os.getenv('api_url', 'http://localhost:8081/api')

def test_connected():
    return requests.get(BASE_URL)

def get_base_headers():
    headers = {
        'Accept': 'application/json',
    }
    
    return headers

def get_base_body(username, password=None, access_id=None):
    body = {}

    if access_id is not None:
        body['access_id'] = access_id
    elif password is not None:
        body['access_id'] = login_user(username=username, password=password).json()['access_id']
    else:
        raise Exception('Username & Password or Username & Access Token not defined')
    
    return body

def create_user(username, password):
    headers = get_base_headers()
    body = {
        "username": username,
        "password": password
    }

    return requests.post(BASE_URL + '/user/register', headers=headers, json=body)

def login_user(username, password):
    headers = {'Accept': 'application/json'}
    body = {
        "username": username,
        "password": password
    }

    return requests.post(BASE_URL + '/user/login', headers=headers, json=body)

def delete_user(username, password=None, access_id=None):
    headers = get_base_headers()

    body = get_base_body(username, password, access_id)
    body['username'] = username
    body['password'] = password

    return requests.post(BASE_URL + '/user/delete',
                             headers=headers,
                             json=body)


def lists_get(username, password=None, access_id=None, id=None, ):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    if id:
        body['id'] = id
    
    return requests.post(BASE_URL + '/list/list', headers=headers, json=body)

def lists_create(username, password=None, access_id=None, name=None, description=None, is_done=False):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    body['name'] = name
    body['description'] = description
    
    return requests.post(BASE_URL + '/list/create', headers=headers, json=body)
    
def lists_delete(username, password=None, access_id=None, name=None):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    body['name'] = name
    
    return requests.post(BASE_URL + '/list/delete', headers=headers, json=body)

def task_get(username, password=None, access_id=None, id=None, list_id=None):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    if id:
        body['id'] = id
    elif list_id:
        body['list_id'] = list_id
    
    return requests.post(BASE_URL + '/task/list', headers=headers, json=body)

def task_create(username, password=None, access_id=None, list_id=None, name=None, description=None):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    
    if list_id:
        body['list_id'] = list_id
    if name:
        body['name'] = name
    if description:
        body['description'] = description
    
    return requests.post(BASE_URL + '/task/create', headers=headers, json=body)

def task_set_done(username, password=None, access_id=None, id=None):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    
    if id:
        body['id'] = id
    
    return requests.post(BASE_URL + '/task/setdone', headers=headers, json=body)

def task_delete(username, password=None, access_id=None, id=None):
    headers = get_base_headers()
    
    body = get_base_body(username, password, access_id)
    if id:
        body['id'] = id

    return requests.post(BASE_URL + '/task/delete', headers=headers, json=body)

if __name__ == '__main__':
    #print(task_get(username='test1', password='test1', id=1).json())
    #print(task_create('test1', 'test1', None, 1, None, 'test1', 'test1').json())
    #print(task_delete('test1', 'test1', None, 4).json())
    pass