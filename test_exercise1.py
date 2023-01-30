from imports_test import *
from secrets_env import HOSTPORT

def test_ping():
    response = requests.get(HOSTPORT + "/ping")
    assert response.json() == {"response": "ping"}
    assert response.status_code == 200