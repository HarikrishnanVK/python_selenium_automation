from behave import *
from assertpy import assert_that
from behaveSample.features.pages.bupa_page import Bupa_Page


def bupa_page(context) -> Bupa_Page:
    global bupa
    bupa = Bupa_Page(context)
    return bupa


@given('I open our bupa link')
def open_link(context):
    bupa_page(context).navigate_to_link()


@then('I verify the page title')
def verify_page_title(context):
    actual_title = context.driver.title
    expected_title = "Our purpose, helping people live healthier | Bupa.com"
    assert_that(expected_title).is_equal_to(actual_title)


@given('I am on landing page')
def verify_homepage(context):
    # bupa = Bupa_Page(context)
    # page_displayed = bupa.verify_homepage()
    # assert_that(page_displayed).is_true()

    page_displayed = bupa_page(context).verify_homepage()
    assert_that(page_displayed).is_true()


@when('I mouse hover on customer websites dropdown')
def mouse_hover_on_customer_service_link(context):
    bupa_page(context).do_mouse_hover(bupa.countries_link)
    print("Mouse hover on dropdown link completed")


@when('I click on customer websites link')
def click_on_dd(context):
    bupa_page(context).do_click(bupa.countries_link)
    print("Dropdown link is opened")


@when('I select "{data}" from dropdown')
def select_dropdown_data(context, data):
    bupa_page(context).select_countries(data)
    context.country = data
    print("Data from dropdown is selected")


@when('I navigate using "{button_name}" associated with country link')
def go_to_country(context, button_name):
    bupa_page(context).navigate_to_country(button_name)
    print(f'navigated to {context.country} using {button_name} button')


@then('I verify the "{page_title}" of the country')
def verify_page(context, page_title):
    page_title: str = str(page_title).replace("->", "|")
    bupa_page(context).switch_to_latest_window()
    actual_title = bupa_page(context).get_page_title()
    assert_that(page_title).is_equal_to(actual_title)
    print(f'found page title as {actual_title}')
