from playwright.sync_api import Page, Locator

from src.pages.added_task_widget import AddedTaskWidget
from src.pages.base_page import BasePage


class TodosPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/todomvc/#/")

        self.input_task_field: Locator = page.locator("//header//input")
        self.added_tasks_list: AddedTaskWidget = AddedTaskWidget(page.locator("//ul[@class='todo-list']//div"))