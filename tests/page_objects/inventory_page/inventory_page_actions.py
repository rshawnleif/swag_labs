from tests.page_objects.base_page import BasePage
from tests.page_objects.inventory_page.inventory_page_elements import InventoryPageElements as loc

class InventoryPageActions(BasePage):
    """This class performs contains all the methods on the Inventory page"""

    def verify_menu_button(self):
        """Performs verifying if the Menu button is visible on the page"""
        assert self.is_visible(loc.menu_button_xpath)

    def verify_app_logo(self):
        """Performs verifying if the app logo is visible on the page"""
        assert self.is_visible(loc.app_logo_xpath)

    def verify_cart_button(self):
        """Performs verifying if the Cart button is visible on the page"""
        assert self.is_visible(loc.cart_button_xpath)

    def click_menu_button(self):
        """Performs clicking the Cart button"""
        self.click_element(loc.menu_button_xpath)

    def click_nav_menu_item(self, item):
        """Performs clicking an item on the navigation menu"""
        self.click_element(loc.nav_menu_items.format(item))

    def verify_product_img(self, img):
        """Verifies if the bug image (bulldog) is observed"""
        assert self.is_visible(loc.product_img_xpath.format(img))