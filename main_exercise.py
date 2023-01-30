from exercise1 import *
from exercise2 import *
from exercise3 import *
from secrets_env import HOST, PORT

if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)
