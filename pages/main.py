
from .base import _PBase
from .locators import main as Locators
from pages import chunks
from tools.test.logger import get_log

log = get_log()


class _PMain(_PBase):
    def __init__(self, *args, **kwargs):
        self.primary_element = None
        self.page_path = ''
        super().__init__(*args, **kwargs)

    def open_elements(self):
        log.step('Open Elements page', where='Portal')
        self.get_object(self.L_BUTTON_ELEMENTS).click()
        left_menu = chunks.get_chunk('left_menu')(self.driver, open_page=False)
        view_checkboxes = chunks.get_chunk('view_checkboxes')(self.driver, open_page=False)
        return left_menu, view_checkboxes


class PMain(_PMain, Locators.LMain):
    pass
