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
driver.get("https://www.ebay.com")
sleep(4)

driver.find_element(By.CSS_SELECTOR,".vl-flyout-nav__link-container[href='https://www.ebay.com/ebaylive']").click()

driver.quit()
