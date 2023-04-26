import logging
import os
import shutil
import allure

import consts


log = None


class CustomLogger(logging.Logger):
    def step(self, msg, where=''):
        if where:
            assert where in consts.STEPS_PLACES, f'Неизвестное место, используйте {", ".join(consts.STEPS_PLACES)}'
        _msg = f'{where}: {msg}' if where else msg
        self.log(consts.LOG_STEP_LEVEL, _msg)
        if where != 'ASSERT': # to avoid double logging
            with allure.step(_msg): pass

    def tc(self, number):
        self.log(logging.INFO, f'Running test case with TestRail number: {number}')


def init_file_handler(level):
    formatter_info_debug = logging.Formatter('%(asctime)s - %(levelname)s:%(filename)s:%(lineno)d - %(message)s')
    formatter_step = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    if level == logging.INFO:
        fname = consts.LOG_INFO
        formatter = formatter_info_debug
    if level == logging.DEBUG:
        fname = consts.LOG_DEBUG
        formatter = formatter_info_debug
    if level == consts.LOG_STEP_LEVEL:
        fname = consts.LOG_STEP
        formatter = formatter_step

    fh = logging.FileHandler(fname, 'w')
    fh.setFormatter(formatter)
    fh.setLevel(level)
    return fh


def get_log():
    global log
    if not log:
        log = _get_log()
    return log


def rm_local_log(leave_folder = True):
    os.path.exists(consts.LOGS_FOLDER) and shutil.rmtree(consts.LOGS_FOLDER)
    leave_folder and os.mkdir(consts.LOGS_FOLDER)


def _get_log():
    not os.path.exists(consts.LOG_DIR) and os.mkdir(consts.LOG_DIR)

    logging.addLevelName(consts.LOG_STEP_LEVEL, 'STEP')
    logging.setLoggerClass(CustomLogger)
    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    fh_debug = init_file_handler(logging.DEBUG)
    logger.addHandler(fh_debug)

    fh_info = init_file_handler(logging.INFO)
    logger.addHandler(fh_info)

    fh_step = init_file_handler(consts.LOG_STEP_LEVEL)
    logger.addHandler(fh_step)
    return logger
