from selenium import webdriver

from tools.test.logger import get_log

log = get_log()


OPTIONS_CHROME_DEFAULT = [
    '--incognito',
]

def generate_chrome_options():
    options = webdriver.ChromeOptions()
    options_list = []
    options_list += OPTIONS_CHROME_DEFAULT
    options.add_argument('ignore-certificate-errors')

    log.info(f'Set Chrome options: {",".join(options_list)}')
    [options.add_argument(el) for el in options_list]
    return options
