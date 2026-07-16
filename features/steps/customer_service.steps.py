from multiprocessing import context

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open customer service page')
def open_customer_service_page(context):
    context.driver.get('https://www.hktvmall.com/hktv/en/cs-help')


@then('Verify that all major elements are present')
def verify_UI_elements(context):
    context.driver.find_element(By.CSS_SELECTOR,'.top-section-text')
    context.driver.find_element(By.ID,'chatbotContainer')
    context.driver.find_element(By.CSS_SELECTOR,'.message')
    context.driver.find_element(By.CSS_SELECTOR,'.ba')
    context.driver.find_element(By.ID,'Salesforce-cshelp')