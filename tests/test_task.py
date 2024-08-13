import pytest
from src.pages.login_page import LoginPage
import uuid

PASSWORD = "pwd"


@pytest.mark.usefixtures("setup")
class TestTask:
    @pytest.fixture(scope="class")
    def login_page(self, setup):
        return LoginPage(setup)

    def test_login_page(self, login_page):
        assert login_page.login_button.is_visible(), "Login page is not displayed"

    @pytest.mark.parametrize("username", [f"user_{uuid.uuid4().hex[:8]}"])
    def test_login(self, login_page, username):
        login_page.login(username, PASSWORD)
        login_page.assert_login_successful(username)

    def test_logout(self, login_page):
        username = f"user_{uuid.uuid4().hex[:8]}"
        login_page.login(username, PASSWORD)
        login_page.logout()
        login_page.assert_logout_successful()
