from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open TVmall main page')
def open_tvmall(context):
    context.driver.get("https://www.hktvmall.com/hktv/en/")
    sleep(5)

@when('Search for a product')
def search_for_product(context):
    context.driver.find_element(By.CSS_SELECTOR,'.SuggestionSearch-input').send_keys('bag')
    context.driver.find_element(By.CSS_SELECTOR,'.magnifier').click()


@when('Click on shopping cart')
def click_on_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'.btn-cart').click()
    sleep(5)


@when('Click on login icon')
def click_on_login_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'.btn-login').click()
    sleep(5)


@then('Verify correct search result shown')
def verify_search_result(context):
    actual = context.driver.find_element(By.CSS_SELECTOR,'.cat_breadcrumb-disabled').text
    expected = "All Products"
    assert expected in actual, f'expected {expected} but got {actual}'


@then('Verify cart is empty')
def verify_empty_cart(context):
    text_displayed = context.driver.find_element(By.CSS_SELECTOR,'.CartEmptyTitle').text
    assert 'empty' in text_displayed, f'expected empty, but got {text_displayed}'


@then('Verify login page is open')
def verify_login_page(context):
    exp_msg = 'Existing Customer'
    actual_msg = context.driver.find_element(By.CSS_SELECTOR,'.login-section-header').text
    assert exp_msg in actual_msg, f'expected {exp_msg} but got {actual_msg}'