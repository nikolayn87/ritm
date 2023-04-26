from .left_menu import CLeftMenu
from .view_checkboxes import CViewCheckBoxes


def get_chunk(chunk_name):
    if chunk_name == 'left_menu':
        return CLeftMenu
    if chunk_name == 'view_checkboxes':
        return CViewCheckBoxes
