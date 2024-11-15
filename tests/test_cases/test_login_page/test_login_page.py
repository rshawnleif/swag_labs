from tests.test_cases.test_base import BaseTest
from tests.page_objects.login_page.login_page_actions import LoginPageActions
from tests.page_objects.inventory_page.inventory_page_actions import InventoryPageActions
from tests.config.test_data import LoginFunctionalityData as login_data
from tests.config.test_data import InventoryFunctionalityData as inventory_data

class TestLoginFunctionality(BaseTest):
    """Test the Login functionality"""

    def test_login_happy_flow(self):
        """Performs logging in using valid username and password"""

        # ARRANGE 
        login_page = LoginPageActions(self.driver)
        inventory_page = InventoryPageActions(self.driver)

        # TEST DATA
        valid_username = login_data.users["standard"]
        valid_password = login_data.password["valid"]

        # ACT
        login_page.input_username(valid_username)
        login_page.input_password(valid_password)
        login_page.click_login_button()

        # ASSERT 
        inventory_page.verify_cart_button()
        inventory_page.verify_app_logo()
        inventory_page.verify_menu_button()

    def test_switch_account_happy_flow(self):
        """Performs Switching of Accounts using valid username and password"""

        # ARRANGE
        login_page = LoginPageActions(self.driver)
        inventory_page = InventoryPageActions(self.driver)

        # TEST DATA
        first_user = login_data.users["standard"]
        second_user = login_data.users["visual"]
        password = login_data.password["valid"]
        nav_item = inventory_data.nav_menu_items["logout"]
        correct_prod_img = inventory_data.product_img["correct_img"]
        incorrect_prod_img = inventory_data.product_img["incorrect_img"]

        # PRE-CONDITION
        """Loggin in using the standard_user account"""
        login_page.input_username(first_user)
        login_page.input_password(password)
        login_page.click_login_button()
        inventory_page.verify_product_img(correct_prod_img)
        inventory_page.click_menu_button()
        inventory_page.click_nav_menu_item(nav_item)
        login_page.verify_login_button()

        # ACT
        """Logging in using the visual_user account"""
        login_page.input_username(second_user)
        login_page.input_password(password)
        login_page.click_login_button()

        # ASSERT
        """Verifying the visual bug on the inventory page of the logged in user"""
        inventory_page.verify_cart_button()
        inventory_page.verify_product_img(incorrect_prod_img)

    def test_login_empty_required_fields(self):
        """Peforms the sad flow of logging in due to empty required fields"""

        # ARRANGE 
        login_page = LoginPageActions(self.driver)

        # TEST DATA
        valid_username = login_data.users["standard"]
        err_username_req = login_data.login_error_msg["username_required"]
        err_password_req = login_data.login_error_msg["password_required"]

        # ACT
        """Performs first the clicking of Login button with empty username"""
        login_page.click_login_button()

        # ASSERT 
        """Verifying the error message about required username"""
        login_page.verify_login_error_message(err_username_req)

        # ACT
        """Performs next the clicking of Login button with filled in username but empty password"""
        login_page.input_username(valid_username)
        login_page.click_login_button()

        # ASSERT 
        """Verifying the error message about required username"""
        login_page.verify_login_error_message(err_password_req)

    def test_login_incorrect_password(self):
        """Performs the sad flow of logging in due to incorrect password"""

        # ARRANGE 
        login_page = LoginPageActions(self.driver)

        # TEST DATA
        valid_username = login_data.users["standard"]
        invalid_password = login_data.password["invalid"]
        error_message = login_data.login_error_msg["incorrect_creds"]

        # ACT
        login_page.input_username(valid_username)
        login_page.input_password(invalid_password)
        login_page.click_login_button()

        # ASSERT 
        login_page.verify_login_error_message(error_message)

    
    def test_login_incorrect_username(self):
        """Performs the sad flow of logging in due to incorrect username"""

        # ARRANGE 
        login_page = LoginPageActions(self.driver)

        # TEST DATA
        invalid_username = login_data.users["invalid_username"]
        valid_password = login_data.password["valid"]
        error_message = login_data.login_error_msg["incorrect_creds"]

        # ACT
        login_page.input_username(invalid_username)
        login_page.input_password(valid_password)
        login_page.click_login_button()

        # ASSERT 
        login_page.verify_login_error_message(error_message)