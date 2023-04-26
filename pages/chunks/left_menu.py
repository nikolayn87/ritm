from pages.base import _PBase
from pages.locators.chunks import left_menu as Locators
from tools.test.logger import get_log

log = get_log()


class _CLeftMenu(_PBase):
    def __init__(self, *args, **kwargs):
        self.primary_element = None
        self.page_path = ''
        super().__init__(*args, **kwargs)

    def open_checkboxes(self):
        self.get_object(self.L_BUTTON_CHECKBOXES).click()


class CLeftMenu(_CLeftMenu, Locators.LLeftMenu):
    pass

