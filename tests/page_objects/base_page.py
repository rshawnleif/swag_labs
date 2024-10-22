from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """This class contains all the generic methods and utilitizd of all pages"""

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, locator)))
        return element

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def click_element(self, locator):
        element = self.get_element(locator)
        element.click()

    def base_send_keys(self, locator, text):
        element = self.get_element(locator)
        element.send_keys(text)

    def get_element_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def is_visible(self, locator):
        element = self.get_element(locator)
        return bool(element)
