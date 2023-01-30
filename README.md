## Installation
Verify that your currently running at least Python 3.9

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required imports.

```bash
#install required imports
pip install -r requirements.txt
#create required secrets_env.py bash
touch secrets_env.py
```

Please remember copy the secrets_env vars into the file
## Usage
Please open a new Terminal window to run flask server and create the data.db file:

```bash
# run flask server
python main_exercise.py
```
On a new Terminal window/tab while flask running in the background:
```bash
# run unit test cases
python main_test_unit_cases.py
```
```bash
# run unit E2E cases
python main_test_E2E_cases.py
```
MAXIMILIANO FONSECA - maxfonseca.r@gmail.com