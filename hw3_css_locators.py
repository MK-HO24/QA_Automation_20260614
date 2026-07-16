from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()


# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()




#open the url
driver.get("https://stackoverflow.com/users/signup")
sleep(20)

driver.find_element(By.CSS_SELECTOR, '.flex--item .fs-headline1')
driver.find_element(By.CSS_SELECTOR, '.flex--item .js-terms')
driver.find_element(By.ID, 'email')
driver.find_element(By.ID, 'password')
driver.find_element(By.ID, 'submit-button')
driver.find_element(By.CSS_SELECTOR, "[data-provider='google']")
driver.find_element(By.CSS_SELECTOR, "[data-provider='github']")
driver.find_element(By.CSS_SELECTOR, "[href*='https://stackoverflow.com/teams?utm_']")