from imports_test import *
from secrets_env import SECRET_KEY, HOSTPORT

def test_authorize():
    response = requests.get(f"{HOSTPORT}/authorize")
    assert response.status_code == 401
    assert response.json() == {"error": "Unauthorized"}

    response = requests.get(f"{HOSTPORT}/authorize", headers={"Authorization": SECRET_KEY})
    assert response.status_code == 200
    assert response.json() == {"response": "Authorized"}