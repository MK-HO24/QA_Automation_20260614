from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open TVmall main page')
def open_tvmall(context):
    context.driver.get("https://www.hktvmall.com/hktv/en/")
    sleep(5)

@when('Search for a {product}')
def search_for_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR,'.SuggestionSearch-input').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR,'.magnifier').click()


@when('Click on shopping cart')
def click_on_shopping_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'.btn-cart').click()
    sleep(5)


@when('Click on login icon')
def click_on_login_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'.btn-login').click()
    sleep(5)


@when('Close pop up message')
def close_popup(context):
    context.driver.find_element(By.CSS_SELECTOR,'.btnCloseLarge').click()


@when('Verify header has {num} links')
def verify_header_links(context, num):
    links = context.driver.find_elements(By.CSS_SELECTOR,"div.account a[class*='btn-']")
    print(links)
    assert len(links) == int(num), f'expected {num} links, got {len(links)}'


@when('Verify header is shown')
def verify_header(context):
    context.driver.find_element(By.CSS_SELECTOR,'div.navi.wrapper')


@when('Verify header has links')
def verify_header_links(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div.account a[class*='btn-']")
    assert len(links) > 0
