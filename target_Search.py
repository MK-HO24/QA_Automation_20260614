from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from time import sleep

# Configure chrome options if you need them (e.g., passing incognito or headless)
options = uc.ChromeOptions()
# options.add_argument("--incognito") # Uncomment if you still need incognito

# Launch the browser using undetected_chromedriver
# Note: It automatically manages the matching driver binary version for you!
driver = uc.Chrome(options=options)

# Maximize the window as requested
driver.maximize_window()

# --- Your test steps go here ---
driver.get("https://target.com")
sleep(5) # Dynamic waits are preferred, but keeping sleep here for your layout


# # populate search field
# search = driver.find_element(By.ID, 'search')
# search.clear()
# search.send_keys('tea')
# driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
# sleep(5)
#
#
# actual_result = driver.find_element(By.XPATH,"//span[@data-test='text-quill-insert-1']").text
# expected_result = 'tea22'
#
# assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
# print(f'{expected_result} is in search result')
#
# driver.quit()


driver.find_element(By.ID,'account-sign-in').click()
sleep(4)
driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()
sleep(4)
expected_text = 'Continue'
actual_text = driver.find_element(By.ID, 'login').text

assert expected_text == actual_text, print(f'{expected_text} != {actual_text}')
print(f'{expected_text} ==> {actual_text}')

#alternative check
driver.find_element(By.XPATH, "//h1[@text='Sign in or create account']")

