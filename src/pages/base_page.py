import configparser

from playwright.sync_api import Page, Locator


class BasePage:

    def __init__(self, page: Page, url_extension: str):
        self.page = page
        self.url_extension = url_extension


    def open(self):
        config= configparser.ConfigParser()
        config.read('pytest.ini')
        base_url =  config["pytest"]["ui_base_url"]
        self.page.goto(base_url + self.url_extension)


    def wait_for_page_load(self):
        self.page.wait_for_load_state("networkidle")