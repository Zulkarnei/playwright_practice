from src.pages.base_page import BasePage
import logging


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = page.locator("#login")
        self.username_field = page.locator("[name='UserName']")
        self.password_field = page.locator("[name='Password']")
        self.login_status = page.locator("#loginstatus")

    def login(self, username, password):
        logging.info(f"Attempting to login with username: {username}")
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
        logging.info("Login button clicked")

    def get_login_status(self):
        return self.login_status.text_content()

    def logout(self):
        logging.info("Logging out")
        self.login_button.click()
        logging.info("Logout button clicked")

    def assert_login_successful(self, expected_username):
        welcome_message = self.get_login_status()
        assert welcome_message == f"Welcome, {expected_username}!", f"Expected 'Welcome, {expected_username}!', but got {welcome_message}"

    def assert_logout_successful(self):
        logout_message = self.get_login_status()
        assert logout_message == "Invalid username/password", f"Expected 'User logged out.', but got {logout_message}"
