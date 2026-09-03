from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target product {product_id} page')
def open_product_page(context):
    context.driver.get('context.base_url/{product_id}')



@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['red', 'green', 'blue']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        sleep(1)


    selected_color = context.driver.find_element(*SELECTED_COLOR).text
    print('Current color',selected_color)

    selected_color = selected_color.split('\n')(1)
    actual_colors.append(selected_color)
    print(actual_colors)

    assert expected_colors == actual_colors, f'Expected colors {expected_colors} did not match {actual_colors}'