from selenium import webdriver
import pytest


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    print("-----------Test SetUp--------------")
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        web_driver = webdriver.Chrome()
    # elif request.param == "firefox":
    #     web_driver = webdriver.Firefox()
    # elif request.param == "edge":
    #     web_driver = webdriver.Edge()
    web_driver.implicitly_wait(10)
    web_driver.delete_all_cookies()
    web_driver.get("https://bupa.com")
    web_driver.maximize_window()
    request.cls.driver = web_driver
    yield web_driver
    print("-----------Test Teardown---------------")
    web_driver.quit()
