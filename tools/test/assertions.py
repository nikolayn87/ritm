import allure
from tools.test.logger import get_log


log = get_log()


def assert_fn(checker, message):
    log.step(message, where='ASSERT')
    with allure.step(message):
        assert checker(), message
