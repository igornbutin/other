# startpage https://krisha.kz/arenda/komnaty/?das[price][to]=70000

# import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Open the URL in Chrome browser
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
driver.get('https://krisha.kz/a/show/679724184')

# Click on the 'show phones' button and wait for the phone number to appear
show_phones_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'show-phones')))
show_phones_button.click()

phone_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'offer__contacts-phones')))

# Get the phone number text from the element
number = phone_number.text.strip()

# Print the phone number
print(number)

# Close the browser window
driver.quit()