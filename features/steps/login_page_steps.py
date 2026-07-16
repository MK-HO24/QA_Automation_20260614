from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify login page is open')
def verify_login_page(context):
    exp_msg = 'Existing Customer'
    actual_msg = context.driver.find_element(By.CSS_SELECTOR,'.login-section-header').text
    assert exp_msg in actual_msg, f'expected {exp_msg} but got {actual_msg}'