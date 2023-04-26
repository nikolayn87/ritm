import pytest

import pages
from tools.test.logger import get_log
from pages import chunks
from tools import aut

log = get_log()


@pytest.mark.smoke
def test_test(setup):
    log.tc('TESTCASE-ID-1')

    driver = aut.start()
    driver.maximize_window()

    main_page = pages.get_page('main')(driver)
    left_menu, view_checkboxes = main_page.open_elements()
    left_menu.open_checkboxes()
    view_checkboxes.pick_file('Home-Downloads-Word File.doc')

    driver.quit()


