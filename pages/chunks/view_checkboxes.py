import re

from pages.base import _PBase
from pages.locators.chunks import view_checkboxes as Locators
from tools.test.logger import get_log

log = get_log()


class _CViewCheckBoxes(_PBase):
    def __init__(self, *args, **kwargs):
        self.primary_element = None
        self.page_path = ''
        super().__init__(*args, **kwargs)

    def expand_tree(self, path):
        expander = '//span[descendant::*[text()="REPLACEME"]]/button'
        loc_method = 'xpath'
        for path_item in path.split('-'):
            loc_value = expander.replace('REPLACEME', path_item)
            self.get_object((loc_method, loc_value)).click()

    def pick_file(self, path):
        _path = path.split('-')[:-1]
        _path = '-'.join(_path)
        _filename = path.split('-')[-1]
        loc_method = 'xpath'
        loc_value = f'//label[descendant::*[text()="{_filename}"]]/span[@class="rct-checkbox"]'

        self.expand_tree(_path)
        checkbox = self.get_object((loc_method, loc_value))
        checkbox.click()
        assert 'rct-icon-check' in checkbox.get_attribute('innerHTML'), 'Checkbox not selected'
        loc_value = '//div[@id="result"]'
        text_list = re.split('\s', self.get_object((loc_method, loc_value)).text)
        assert text_list == ['You', 'have', 'selected', ':', 'wordFile'], 'Text is wrong'


class CViewCheckBoxes(_CViewCheckBoxes, Locators.LViewCheckBoxes):
    pass

