from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Base_Methods:
    driver: webdriver.Chrome

    def __int__(self, driver):
        self.driver = driver

    def __wait(self):
        return WebDriverWait(self.driver, 30, poll_frequency=3, ignored_exceptions=StaleElementReferenceException)

    def __find_element(self, by_locator):
        try:
            locator_type, selector = str(by_locator).split("=>")
        except():
            raise Exception("unable to parse the " + by_locator + " . Please check the format")
        selector = str(selector).strip()
        match str(locator_type).lower().strip():
            case "id":
                self.__wait().until(EC.visibility_of_element_located((By.ID, selector)))
                element = self.driver.find_element(By.ID, selector)
            case "xpath":
                self.__wait().until(EC.visibility_of_element_located((By.XPATH, selector)))
                element = self.driver.find_element(By.XPATH, selector)
            case "css":
                self.__wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                element = self.driver.find_element(By.CSS_SELECTOR, selector)
            case _:
                raise Exception(locator_type + " is not added to webelement generic")
        return element

    def __find_elements(self, by_locator):
        locator_type, selector = str(by_locator).split("=>")
        selector = str(selector).strip()
        match str(locator_type).lower().strip():
            case "id":
                self.__wait().until(EC.visibility_of_element_located((By.ID, selector)))
                elements = self.driver.find_elements(By.ID, selector)
            case "xpath":
                self.__wait().until(EC.visibility_of_element_located((By.XPATH, selector)))
                elements = self.driver.find_elements(By.XPATH, selector)
            case "css":
                self.__wait().until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
            case _:
                raise Exception(locator_type + " is not added to list of webelement generic")
        return elements

    def do_click(self, by_locator):
        element = self.__find_element(by_locator)
        element.click()

    def _enter_data(self, by_locator, data):
        element = self.__find_element(by_locator)
        element.clear()
        element.send_keys(data)
        element.send_keys(Keys.ENTER)

    def do_mouse_hover(self, by_locator):
        element = self.__find_element(by_locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def _get_text(self, by_locator, text_to_wait_till_appear="none"):
        locator_type, selector = str(by_locator).split("=>")
        self.__wait().until(EC.text_to_be_present_in_element((By.XPATH, selector), text_to_wait_till_appear))
        element = self.__find_element(by_locator)
        return element.text

    def _get_attribute(self, by_locator, property_name):
        element = self.__find_element(by_locator)
        return element.get_attribute(property_name)

    def _click_using_text_from_list(self, by_locator, text):
        elements = self.__find_elements(by_locator)
        for element in elements:
            try:
                if element.text == text:
                    element.click()
                    break
            except StaleElementReferenceException:
                print('stale element exception handled')

    def get_page_title(self) -> str:
        return self.driver.title

    def _is_element_displayed(self, by_locator) -> bool:
        return self.__find_element(by_locator).is_displayed()

    def select_data_from_dd(self, option, selector, data):
        element = self.__find_element(selector)
        match str(option).lower():
            case "index":
                Select(element).select_by_index(data)
            case "value":
                Select(element).select_by_value(data)
            case "text":
                Select(element).select_by_visible_text(data)
            case _:
                raise Exception(f'{option} is not part of dropdown match case')

    def switch_to_latest_window(self):
        current_window = self.driver.current_window_handle
        handles = self.driver.window_handles
        for handle in handles:
            if handle != current_window:
                self.driver.switch_to.window(handle)

    def switch_to_window_by_title(self, win_title):
        handles = self.driver.window_handles
        for handle in handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == win_title:
                break
            else:
                self.driver.switch_to.default_content()
                continue
