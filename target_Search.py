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

# --- Your test steps go here ---
driver.get("https://target.com")
sleep(5) # Dynamic waits are preferred, but keeping sleep here for your layout


# # populate search field
search = driver.find_element(By.ID, 'search')
search.clear()
search.send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)


actual_result = driver.find_element(By.XPATH,"//span[@data-test='text-quill-insert-1']").text
expected_result = 'tea22'

assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
print(f'{expected_result} is in search result')

driver.quit()




