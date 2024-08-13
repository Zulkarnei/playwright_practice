from .base_page import BasePage


class SampleAppPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.login_button = page.locator("#login")
        self.username_field = page.locator("[name='UserName']")
        self.password_field = page.locator("[name='Password']")
        self.login_status = page.locator("#loginstatus")

    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()

    def get_login_status(self):
        return self.login_status.text_content()

    def logout(self):
        self.login_button.click()
