import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import StaleElementReferenceException
import pytest

driver: webdriver


def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://bupa.com")
    driver.maximize_window()


def teardown_module():
    driver.quit()


def test_navigation():
    print(driver.title)
    action = ActionChains(driver)
    ourBupaLink = driver.find_element(By.CSS_SELECTOR, "li[id='nav-our-bupa-level1'] >  a[href='/our-bupa']")
    action.move_to_element(ourBupaLink).perform()
    ourBupaSubLinks = driver.find_elements(By.CSS_SELECTOR, "ul[id='section-our-bupa-level2']  li[id*=level2]  > a")
    for link in ourBupaSubLinks:
        # linkText = driver.execute_script("return arguments[0].text", link)
        try:
            if link.text == "Our purpose":
                link.click()
                print(link.text + 'is clicked')
                break
        except StaleElementReferenceException:
            print('stale element exception is handled')
            break


def test_search():
    searchButton = driver.find_element(By.CSS_SELECTOR, "nav[class='desktop-nav'] + div > a[class='searchButton']")
    searchButton.click()
    searchBox1 = driver.find_element(By.CSS_SELECTOR, "input[id*='searchTextbox']")
    searchBox1.send_keys("Mitchell Starc")
    searchBox1.send_keys(Keys.ENTER)
    noResultFound = driver.find_element(By.XPATH, "//div[@class='searchresultpage']//div[@id='noresults']//span")
    assert noResultFound.text == "No Results Found"
    searchBox2 = driver.find_element(By.CSS_SELECTOR,
                                     "input[id='solrstrap-searchbox']")
    searchBox2.clear()
    searchBox2.send_keys("Bupa")
    searchBox2.send_keys(Keys.ENTER)
    searchLink = driver.find_element(By.XPATH, "(//span[@class='resultURL']//a)[1]")
    searchLink.click()
    print("Link selected is " + searchLink.get_attribute("href"))
