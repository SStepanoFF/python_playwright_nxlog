import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("task_name", ["task 1", "зробити 2"])
def test_todo_add_task(todos_page, task_name):
    todos_page.open()
    todos_page.input_task_field.type(task_name)
    todos_page.page.keyboard.press("Enter")

    expect(todos_page.added_tasks_list.task_name).to_have_text(task_name)
