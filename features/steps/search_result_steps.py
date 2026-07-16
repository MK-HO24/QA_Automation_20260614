from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then('Verify correct search result shown for {product}')
def verify_search_result(context, product):
    sleep(5)
    # actual = context.driver.find_element(By.XPATH,f"//h1//span[contains(text(), {product})]").text
    actual = context.driver.find_element(By.CSS_SELECTOR,".searchTitle").text
    assert product in actual, f'expected {product} but got {actual}'



