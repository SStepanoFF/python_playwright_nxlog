import pytest
from playwright.sync_api import expect


@pytest.mark.parametrize("task_name", ["task 1", "зробити 2"])
def test_todo_add_task(todos_page, task_name):
    todos_page.open()
    todos_page.input_task_field.type(task_name)
    todos_page.page.keyboard.press("Enter")

    expect(todos_page.get_tasks()[0].task_name).to_have_text(task_name)


def test_todo_complete_task(todos_page):
    # create task
    task_name = "task"
    todos_page.open()
    todos_page.input_task_field.type(task_name)
    todos_page.page.keyboard.press("Enter")
    expect(todos_page.get_tasks()[0].task_name).to_have_text(task_name)

    # complete task
    todos_page.get_tasks()[0].toggle_todo.click()

    # validate
    expect(todos_page.get_tasks()[0].locator).to_have_class("completed")

    # check in Completed
    todos_page.filter_completed_button.click()
    expect(todos_page.get_tasks()[0].task_name).to_have_text(task_name)


def test_todo_delete_task(todos_page):
    # create task
    task_name = "task"
    todos_page.open()
    todos_page.input_task_field.type(task_name)
    todos_page.page.keyboard.press("Enter")
    expect(todos_page.get_tasks()[0].task_name).to_have_text(task_name)

    # delete task
    todos_page.get_tasks()[0].locator.hover()
    todos_page.get_tasks()[0].delete_task.click()

    # validate not present
    expect(todos_page.added_tasks_list).to_have_count(0)


def test_todo_delete_task_in_list(todos_page):
    # create tasks
    task1_name = "task 1"
    task2_name = "task 2"
    todos_page.open()
    todos_page.input_task_field.type(task1_name)
    todos_page.page.keyboard.press("Enter")
    todos_page.input_task_field.type(task2_name)
    todos_page.page.keyboard.press("Enter")
    expect(todos_page.added_tasks_list).to_have_count(2)

    # delete task
    todos_page.get_tasks()[0].locator.hover()
    todos_page.get_tasks()[0].delete_task.click()

    # validate not present
    expect(todos_page.added_tasks_list).to_have_count(1)
    expect(todos_page.added_tasks_list.filter(has_text=task1_name)).not_to_be_visible()

    #check task2 is still present
    expect(todos_page.added_tasks_list.filter(has_text=task2_name)).to_be_visible()

    # check all tabs
    todos_page.filter_completed_button.click()
    expect(todos_page.added_tasks_list.filter(has_text=task1_name)).not_to_be_visible()

    todos_page.filter_active_button.click()
    expect(todos_page.added_tasks_list.filter(has_text=task1_name)).not_to_be_visible()
