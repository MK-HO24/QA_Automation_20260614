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
driver.get("https://www.amazon.com")
sleep(4)
driver.find_element(By.XPATH, "//div[@id='nav-link-accountList']//a[@data-nav-role='signin']").click()

driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")
driver.find_element(By.ID, 'ap_email_login')
driver.find_element(By.XPATH, "//input[@class='a-button-input']")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")
driver.find_element(By.XPATH,"//span[@class='a-list-item']")
driver.find_element(By.ID, 'ab-registration-ingress-link')

driver.find_element(By.XPATH, "//a[text()='Conditions of Use']").click()
sleep(4)