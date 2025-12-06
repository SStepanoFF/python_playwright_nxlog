import allure
from playwright.sync_api import Page

import pytest
from playwright.sync_api import sync_playwright

from src.pages.todos_page import TodosPage


@pytest.fixture(scope="session")
def playwright():
    p = sync_playwright().start()
    yield p
    p.stop()


@pytest.fixture(scope="session")
def browser(playwright, request):
    browser_name = request.config.getoption("--browser-name") or request.config.getini("browser")
    headless = request.config.getoption("--headless") or request.config.getini("headless")

    browser = playwright.chromium.launch(
        channel=browser_name,
        headless=str(headless).lower() == "true",
        args=["--disable-gpu", "--use-angle=metal"]
    )

    yield browser
    browser.close()


@pytest.fixture
def browser_context(browser):
    context = browser.new_context()   # Fresh clean profile
    yield context
    context.close()


@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()


def pytest_addoption(parser):
    parser.addini("browser", "Browser to use for tests", default="chrome")
    parser.addini("headless", "Run in headless mode", default="false")
    parser.addini("ui_base_url", "Base url for UI tests", default=None)

    parser.addoption("--browser-name", action="store", help="Override browser from CLI")
    parser.addoption("--headless", action="store", help="Override headless mode true/false")


@pytest.fixture
def todos_page(page: Page):
    return TodosPage(page)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            allure.attach(
                page.screenshot(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

            allure.attach(
                page.content(),
                name="page_html",
                attachment_type=allure.attachment_type.HTML
            )
