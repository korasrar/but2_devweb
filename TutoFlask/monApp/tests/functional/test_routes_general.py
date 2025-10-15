from monApp import app

def test_index_without_params(client):
    response = client.get('/index/')
    assert response.status_code == 200
    assert b'Cricri' in response.data

def test_index_with_name_param(client):
    response = client.get('/index/?name=TestUser')
    assert response.status_code == 200
    assert b'TestUser' in response.data

def test_about(client):
    response = client.get('/about/')
    assert response.status_code == 200
    assert b'about' in response.data

def test_contact(client):
    response = client.get('/contact/')
    assert response.status_code == 200
    assert b'Contact' in response.data
