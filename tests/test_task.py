import pytest
from src.pages.sample_app_page import SampleAppPage
import uuid

@pytest.mark.usefixtures("setup")
class TestTask:
    @pytest.fixture(scope="class")
    def login_page(self, browser):
        return SampleAppPage(browser)

    def test_login_page(self, login_page):
        assert login_page.login_button.is_visible(), "Login page is not displayed"

    def test_login(self, login_page):
        username = f"user_{uuid.uuid4().hex[:8]}"
        password = "pwd"
        login_page.login(username, password)

        welcome_message = login_page.get_login_status()
        assert welcome_message == f"Welcome, {username}!"


    def test_logout(self, login_page):
        username = f"user_{uuid.uuid4().hex[:8]}"
        password = "pwd"
        login_page.login(username, password)
        login_page.logout()

        logout_message = login_page.get_login_status()
        assert logout_message == "Invalid username/password"