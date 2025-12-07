from playwright.sync_api import Locator


class AddedTaskWidget:

    def __init__(self, locator: Locator):
        self.locator = locator

        self.toggle_todo: Locator = self.locator.locator("//*[@aria-label='Toggle Todo']")
        self.task_name: Locator = self.locator.locator("//*[@data-testid='todo-title']")
        self.delete_task: Locator = self.locator.locator("//*[@aria-label='Delete']")