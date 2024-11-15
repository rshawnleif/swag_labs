import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from webdriver_manager.chrome import ChromeDriverManager
from tests.config.test_data import Initialize as data

@pytest.fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
    request.cls.driver = web_driver

    web_driver.get(url=data.BASE_URL)

    web_driver.implicitly_wait(10)

    web_driver.maximize_window()
    yield
    web_driver.quit()
    