from .main import PMain


def get_page(page_name):
    if page_name == 'main':
        return PMain
