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
# locate element
#driver.find_element()
#locate by id
driver.find_element(By.ID, "nav-global-location-popover-link")
driver.find_element(By.ID, "nav-global-location-toaster-script-container")
#locate by xpath
driver.find_element(By.XPATH, "//span[@class='hm-icon-label']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
#multiple attributes
driver.find_element(By.XPATH, "//a[@class = 'nav-a  ' and contains(text(),'Prime Day')]")
#with text
driver.find_element(By.XPATH, "//a[text()='Health AI']")
#with text and other attribute
driver.find_element(By.XPATH, "//a[text()='Health AI' and @class='nav-a  ']")
#by attribute only, any tag
driver.find_element(By.XPATH, "//*[text()='Health AI']")
#by XPATH, parent node to child node
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container'] //a[@href='https://health.amazon.com/health-ai?ref_=nav_cs_health_ai']")


# driver.find_element(By.XPATH, "//a[@class='a-link-nav-icon']")
