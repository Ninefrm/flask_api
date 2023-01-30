from imports_test import *
from secrets_env import HOSTPORT, SECRET_KEY

def test_ping():
    response = requests.get(HOSTPORT + "/ping")
    assert response.json() == {"response": "ping"}
    assert response.status_code == 200

def test_authorize():
    response = requests.get(HOSTPORT + "/authorize", headers={"Authorization": SECRET_KEY})
    assert response.json() == {"response": "Authorized"}
    assert response.status_code == 200

    response = requests.get(HOSTPORT + "/authorize")
    assert response.json() == {"error": "Unauthorized"}
    assert response.status_code == 401
