import requests
import unittest
import helper

from requests.api import head

def test_connected():
    response = helper.test_connected()
    assert response.status_code == 200
    assert "application/json" in response.headers['Content-Type']
    assert response.json() == {'message': 'Connected!'}

def test_user_register():
    response = helper.create_user('unittest1', 'unittest1')
    assert response.json().get('access_id', None) is not None

    # Cleanup
    helper.delete_user(username='unittest1', password='unittest1')

def test_user_already_exists():
    helper.create_user('unittest1', 'unittest1')
    
    response = helper.create_user('unittest1', 'unittest1')
    assert response.json() == {'errorMsg': 'A user with that username already exists'}

    helper.delete_user(username='unittest1', password='unittest1')

def test_user_login():
    helper.create_user(username='unittest1', password='unittest1')

    response = helper.login_user('unittest1', 'unittest1')
    assert response.json().get('access_id', None) is not None
    
    helper.delete_user(username='unittest1', password='unittest1')

def test_user_delete():
    helper.create_user(username='unittest1', password='unittest1')
    
    response = helper.delete_user(username='unittest1', password='unittest1')
    assert response.json() == {'msg': 'Delete Successful'}

if __name__ == '__main__':
    pass
