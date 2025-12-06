from playwright.sync_api import Locator


class AddedTaskWidget:

    def __init__(self, locator: Locator):
        self.locator = locator

        self.toggle_todo: Locator = self.locator.locator("//input")
        self.task_name: Locator = self.locator.locator("//label")
        self.delete_task: Locator = self.locator.locator("//button")