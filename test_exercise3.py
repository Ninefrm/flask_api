from imports_test import *
from secrets_env import SECRET_KEY, HOSTPORT

def clean_database():
    response = requests.get(f"{HOSTPORT}/setup")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

    response = requests.get(f"{HOSTPORT}/setup", headers={"Authorization": SECRET_KEY})
    assert response.status_code == 200
    assert response.json() == {"response": "Data cleared"}

def test_save_data():
    response = requests.post(f"{HOSTPORT}/save")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

    response = requests.post(f"{HOSTPORT}/save", headers={"Authorization": SECRET_KEY}, json={"id": 1, "data": "test"})
    assert response.status_code == 200 
    assert response.json() == {"response": "Data saved"}

    response = requests.post(f"{HOSTPORT}/save", headers={"Authorization": SECRET_KEY}, json={"id": 1, "data": "test"})    
    assert response.status_code == 400 
    assert response.json() == {"error": "Data exist"}


def test_delete_data():
    response = requests.delete(f"{HOSTPORT}/delete")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

    response = requests.delete(f"{HOSTPORT}/delete", headers={"Authorization": SECRET_KEY}, json={"id": 1})
    assert response.status_code == 200
    assert response.json() == {"response": "Data deleted"}

    response = requests.delete(f"{HOSTPORT}/delete", headers={"Authorization": SECRET_KEY}, json={"id": 1})
    assert response.status_code == 400
    assert response.json() == {"error": "Invalid id"}

def test_get_data():
    response = requests.get(f"{HOSTPORT}/get")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

    response = requests.get(f"{HOSTPORT}/get", headers={"Authorization": SECRET_KEY})
    assert response.status_code == 200
    assert "response" in response.json()
