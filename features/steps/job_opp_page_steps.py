from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Job Opp page')
def open_job_page(context):
    context.driver.get('https://www.hktv.com.hk/join-opportunity')
    sleep(5)


@then('Verify that {num} tiles are shown')
def verify_tiles(context, num):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div.sigma_product")
    print(links)
    assert len(links) == int(num), f'Expected {num} tiles, but found {len(links)}'
