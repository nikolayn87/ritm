from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

from tools.test.config import get_config
from tools.test.config import get_env
from tools.test.logger import get_log
from tools.test.assertions import assert_fn


log = get_log()


def get_env_url():
    conf = get_config()
    env = get_env()
    return conf[env]['web_url']


class _PBase:
    def __init__(self, driver, open_page=True, check_primary_element=True, version=''):
        self.version = version
        self.driver = driver
        self.driver.implicitly_wait(0)
        self.env_url = get_env_url()
        if open_page:
            self.primary_url = self.env_url + self.page_path
            self.open()
        if check_primary_element:
            self.wait_presence(self.primary_element)

    def open(self):
        self.driver.get(self.primary_url)

    def open_url(self, url):
        self.driver.get(url)

    def wait_presence(self, locator, timeout=15, message='', mode='raise'):
        if locator is None:
            return True
        log.debug(f'Start waiting presence of element "{locator}"')
        try:
            _ = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:  # add message for TimeoutException
            _msg = message or f'No such element: {locator[1]}'
            if mode == 'raise':
                raise TimeoutException(_msg)
            if mode == 'return':
                return False
        log.debug(f'Finished waiting presence of element "{locator}"')
        return True

    def get_object(self, locator):
        self.wait_presence(locator)
        try:
            result = self.driver.find_element(*locator)
            result.exists = True
        except NoSuchElementException:
            log.warning(f"Web element with locator '{locator}' doesn't exist")
            raise
        return result

    def assert_presence(self, locator, message):
        fn = lambda: self.wait_presence(locator, message=message, mode='return')
        assert_fn(fn, message)

