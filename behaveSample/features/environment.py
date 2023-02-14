import allure
from selenium import webdriver
from allure_commons.types import AttachmentType


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.get("https://bupa.com")
    context.driver.maximize_window()
    print(f'scenario: {scenario.name} is being executed')
    # context.bupa = Bupa_Page(context)


def before_step(context, step):
    context.step = step


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(), name=context.scenario.name + " " + context.step.name,
                      attachment_type=AttachmentType.PNG)
        print(f'scenario: {scenario.name} is failed and screenshot attached')
    context.driver.quit()
