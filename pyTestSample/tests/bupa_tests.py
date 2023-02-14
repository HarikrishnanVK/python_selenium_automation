import pytest
from pyTestSample.pages.bupa_page import Bupa_Page


@pytest.mark.usefixtures("init_driver")
class TestBupa:

    def bupa(self) -> Bupa_Page:
        return Bupa_Page(self.driver)

    def test_navigation(self):
        self.bupa().navigate_to_link()

    def test_search_with_invalid_data(self):
        self.bupa().do_search("Mitchell Starc")
        actual_text = self.bupa().get_search_result(self.bupa().no_result_text, "No Results Found")
        expected_text = "No Results Found"
        assert expected_text == actual_text, "'" + expected_text + "'" + " not equal to " + "'" + actual_text + "'"

    def test_search_with_valid_data(self):
        self.bupa().do_search("Bupa")
        self.bupa().do_click(self.bupa().search_result_link)
        print("Link selected is " + self.bupa()._get_attribute(self.bupa().search_result_link, "href"))
