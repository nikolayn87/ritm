python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python -m pytest -m smoke --env prod
#allure serve allure-raw &
