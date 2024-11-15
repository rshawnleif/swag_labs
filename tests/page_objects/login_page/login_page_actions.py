from tests.page_objects.base_page import BasePage
from tests.page_objects.login_page.login_page_elements import LoginPageElements as loc

class LoginPageActions(BasePage):
    """This contains all methods on the Login Page"""

    def input_username(self, username):
        """Inputs the username on the Login page"""
        self.base_send_keys(loc.username_xpath, username)

    def input_password(self, password):
        """Inputs the password on the Login page"""
        self.base_send_keys(loc.password_xpath, password)

    def click_login_button(self):
        """Performs clicking the Login button"""
        self.click_element(loc.login_button_xpath)

    def verify_login_button(self):
        """Verifies if the Login button is visible"""
        assert self.is_visible(loc.login_button_xpath)

    def verify_login_error_message(self, error_message):
        """Verify the login error banner"""
        assert self.is_visible(loc.login_error_msg_xpath.format(error_message))