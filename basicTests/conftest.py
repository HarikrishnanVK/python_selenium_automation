import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def init_chrome_driver(request):
    print("-----------Test SetUp--------------")
    web_driver = webdriver.Chrome()
    web_driver.implicitly_wait(10)
    web_driver.delete_all_cookies()
    web_driver.get("https://bupa.com");
    web_driver.maximize_window();
    request.cls.driver = web_driver
    yield
    print("-----------Test Teardown---------------")
    web_driver.quit()


@pytest.fixture(scope="function")
def init_firefox_driver(request):
    print("-----------Test SetUp--------------")
    web_driver = webdriver.Firefox()
    web_driver.implicitly_wait(10)
    web_driver.delete_all_cookies()
    web_driver.get("https://bupa.com");
    web_driver.maximize_window();
    request.cls.driver = web_driver
    yield
    print("-----------Test Teardown---------------")
    web_driver.quit()
