import pytest
from playwright.sync_api import sync_playwright


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="session")
def browser(pytestconfig):
    headless = pytestconfig.getoption("headless")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture(scope="session")
def setup(browser):
    base_url = "http://uitestingplayground.com/sampleapp"
    page = browser.new_page()
    page.goto(base_url)
    yield page
    page.close()
