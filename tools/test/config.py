import sys
import yaml

import consts
from tools.test.logger import get_log


config = None
log = get_log()


def get_config(path = consts.DEFAULT_CONFIG):
    global config
    if not config:
        config = load_config(path)
    return config


def load_config(path):
    with open(path, 'r') as f:
        cfg = yaml.safe_load(f)

    log.info('Test config loaded')
    log.debug(cfg)
    return cfg


def get_env():
    env = None
    for i, arg in enumerate(sys.argv):
        if arg == '--env':
            env = sys.argv[i + 1]
            break
    return env


