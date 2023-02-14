import time
from behaveSample.features.utilities.generic_methods import Base_Methods

class Bupa_Page(Base_Methods):

    def __init__(self, context):
        super().__int__(context.driver)

    our_bupa_link = "CSS => li[id='nav-our-bupa-level1'] >  a[href='/our-bupa']"
    our_bupa_sublinks = "CSS => ul[id='section-our-bupa-level2']  li[id*=level2]  > a"
    search_button = "CSS => nav[class='desktop-nav'] + div > a[class='searchButton']"
    search_box_1 = "CSS => input[id*='searchTextbox']"
    search_box_2 = "CSS => input[id='solrstrap-searchbox']"
    no_result_text = "XPATH => //div[@class='searchresultpage']//div[@id='noresults']//span"
    search_result_link = "XPATH => (//span[@class='resultURL']//a)[1]"
    bupa_logo = "CSS => figure[id='logo'] > img"
    countries_link = "CSS => li[class=dropdown] a[class=websites]"
    countries_dd = "CSS => select[id='select-box']"
    cookies_button = "CSS => button[name=cookieAgree]"

    def navigate_to_link(self):
        """
            navigate to link
        """
        super().do_mouse_hover(self.our_bupa_link)
        super()._click_using_text_from_list(self.our_bupa_sublinks, "Our purpose")
        time.sleep(2)
        actual_title = super().get_page_title()
        expected_title = "Our purpose, helping people live healthier | Bupa.com"
        assert actual_title == expected_title, "'" + actual_title + "'" + " not equal to " + "'" + expected_title + "'"

    def do_search(self, search_text):
        super().do_click(self.search_button)
        super()._enter_data(self.search_box_1, search_text)

    def get_search_result(self, search_result_el, result_to_wait_for="none"):
        actual_text = super()._get_text(search_result_el, result_to_wait_for)
        return actual_text

    def verify_homepage(self) -> bool:
        super().do_click(self.cookies_button)
        return super()._is_element_displayed(self.bupa_logo)

    def select_countries(self, data):
        super().select_data_from_dd("value", self.countries_dd, data)

    def navigate_to_country(self, selector):
        by_locator = f'XPATH => //div[@class="website-button"]//a[contains(text(),"{selector}")]'
        super().do_click(by_locator)

