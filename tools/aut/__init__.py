from selenium import webdriver

import consts
from . import options


def start(local=True):
    opts = options.generate_chrome_options()
    if local:
        return webdriver.Chrome(options=opts)
    
