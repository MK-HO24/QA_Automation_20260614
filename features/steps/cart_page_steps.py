from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


ADD_TO_CART_BUTTON = (By. CSS_SELECTOR,'.icAddtocart')

@when('Add item to cart')
def add_item_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'.icQuickviewmore')), message='Quick view more menu not visible')
    context.driver.find_element(By. CSS_SELECTOR,'div.buttonWrapper').click()


@when('Store item name')
def store_product_name(context):
    context.product_name = context.driver.find_element(By.CSS_SELECTOR,'.prod-name').text
    print(context.product_name)


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

@then('Verify that correct item is added to cart')
def verify_correct_item(context):
    assert 'shirt' in context.product_name, f'expected "Shirt" in summary, but got {context.product_name}'
