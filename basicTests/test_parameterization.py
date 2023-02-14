from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import pytest


@pytest.mark.usefixtures("init_chrome_driver")
class Base_Test():
    pass


class Test_Bupa(Base_Test):
    driver: webdriver.Chrome

    @pytest.mark.parametrize("linkName", ["our-purpose", "Our story", "Our strategy"])
    def test_links(self, linkName):
        driver = self.driver;
        driver.find_element(By.CSS_SELECTOR, "button[name='cookieAgree']").click()
        links = driver.find_elements(By.CSS_SELECTOR, "div[class='footer-box2'] a")
        for link in links:
            try:
                if link.text == linkName:
                    link.click()
                    print(link.text + ' link opened')
                    break
            except:
                StaleElementReferenceException
            print('stale element exception handled')

