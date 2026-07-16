from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Add item to cart')
def add_item_to_cart(context):
    context.driver.find_element(By. CSS_SELECTOR,'.icAddtocart').click()
    context.driver.find_element(By. CSS_SELECTOR,'div.buttonWrapper').click()


@then('Verify cart is empty')
def verify_empty_cart(context):
    text_displayed = context.driver.find_element(By.CSS_SELECTOR,'.CartEmptyTitle').text
    assert 'empty' in text_displayed, f'expected empty, but got {text_displayed}'


@then('Verify that item is added to cart')
def verify_cart_item(context):
    context.driver.get('https://www.hktvmall.com/hktv/en/cart')
    cart_txt = context.driver.find_element(By. CSS_SELECTOR, '.cart-sub-total').text
    print(cart_txt)
    assert "Purchase Amount" in cart_txt, f'expected "Purchase Amount" in Summary, but got {cart_txt}'

