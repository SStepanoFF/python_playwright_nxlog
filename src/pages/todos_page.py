from playwright.sync_api import Page, Locator

from src.pages.added_task_widget import AddedTaskWidget
from src.pages.base_page import BasePage


class TodosPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page, "/todomvc/#/")

        self.input_task_field: Locator = page.locator("//header//input")
        self.filter_all_button: Locator = page.locator("//footer//*[text()='All']")
        self.filter_active_button: Locator = page.locator("//footer//*[text()='Active']")
        self.filter_completed_button: Locator = page.locator("//footer//*[text()='Completed']")
        self.added_tasks_list = page.locator("//*[@data-testid='todo-item']")

    def get_tasks(self) -> list[AddedTaskWidget]:
        count = self.added_tasks_list.count()
        return [
            AddedTaskWidget(self.added_tasks_list.nth(i))
            for i in range(count)
        ]