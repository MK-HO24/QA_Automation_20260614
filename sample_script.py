from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
wait = WebDriverWait(driver,10)


# driver.implicitly_wait(4)
# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Car')

# wait for 4 sec
sleep(4)

"""EC only expect 1 object when it comes to locators. We therefore have to include 
an extra pair of () to encapsulate the 2 objects into 1"""

wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search button not clickable!').click()
# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
