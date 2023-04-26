python3 -m venv venv
source venv/bin/python
python -m pip install -r requirements.txt
python -m pytest -m smoke --env prod
#allure serve allure-raw &
