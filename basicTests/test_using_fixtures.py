from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import pytest

driver = webdriver.Chrome

@pytest.mark.usefixtures("init_chrome_driver")
def test_navigation():
    print(driver.title);
    action = ActionChains(driver)
    ourBupaLink = driver.find_element(By.CSS_SELECTOR, "li[id='nav-our-bupa-level1'] >  a[href='/our-bupa']")
    action.move_to_element(ourBupaLink).perform();
    ourBupaSubLinks = driver.find_elements(By.CSS_SELECTOR, "ul[id='section-our-bupa-level2']  li[id*=level2]  > a")
    for link in ourBupaSubLinks:
        # linkText = driver.execute_script("return arguments[0].text;", link)
        try:
            if link.text == "Our purpose":
                link.click()
                print(link.text + 'is clicked')
                break
        except StaleElementReferenceException:
            print('stale element exception is handled')
            break


def test_search(init_firefox_driver):
    searchButton = driver.find_element(By.CSS_SELECTOR, "nav[class='desktop-nav'] + div > a[class='searchButton']")
    searchButton.click();
    searchBox1 = driver.find_element(By.CSS_SELECTOR, "input[id*='searchTextbox']")
    searchBox1.send_keys("Mitchell Starc")
    searchBox1.send_keys(Keys.ENTER);
    wait = WebDriverWait(driver, 10, poll_frequency=2)
    wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                 "//div[@class='searchresultpage']//div[@id='noresults']//span"),
                                                "No Results Found"))
    actual_text = driver.find_element(By.XPATH, "//div[@class='searchresultpage']//div[@id='noresults']//span").text
    assert actual_text == "No Results Found"
    searchBox2 = driver.find_element(By.CSS_SELECTOR,
                                     "input[id='solrstrap-searchbox']")
    searchBox2.clear()
    searchBox2.send_keys("Bupa")
    searchBox2.send_keys(Keys.ENTER)
    wait.until(EC.presence_of_element_located((By.XPATH, "(//span[@class='resultURL']//a)[1]"))).click()
