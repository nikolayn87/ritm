import re
import pytest
import traceback
import platform

import consts
from tools.test.config import get_config
from tools.test.logger import get_log


log = get_log()
option = None


@pytest.fixture(autouse=True)
def run_around_tests(request):
    test_case = re.findall('Function (.*?)>', str(request.keywords))[0]
    log.step(f'~~~~~START {test_case}~~~~~')
    yield
    log.step(f'~~~~~END {test_case}~~~~~')


@pytest.fixture(scope='session')
def version_reporter():
    # TODO: report version
    log.info('Calling "version_reporter" fixture')


@pytest.fixture(scope='session')
def setup(version_reporter):
    log.info('Calling "setup" fixture')
    log.info(f'Using "{option.env}" environment')
    return {
        'config': get_config()[option.env],
    }


def pytest_runtest_makereport(item, call):
    # logging each traceback to respective testcase
    if call.excinfo:
        tb_obj = call.excinfo.tb
        stack_summary = traceback.extract_tb(tb_obj)
        tb_strings = stack_summary.format()
        tb_string = ''.join(tb_strings)
        tb_string = call.excinfo.exconly() + '\n' + tb_string

        stack_summary_locals = stack_summary.extract(traceback.walk_tb(tb_obj), capture_locals = True)
        tb_strings_locals = stack_summary_locals.format()
        tb_string_locals = ''.join(tb_strings_locals)
        tb_string_locals = call.excinfo.exconly() + '\n' + tb_string_locals

        log.info(tb_string)
        log.debug(tb_string_locals)


def pytest_addoption(parser):
    parser.addoption('--env', action='store', help='Environment name')


def pytest_configure(config):
    global option
    option = config.option
