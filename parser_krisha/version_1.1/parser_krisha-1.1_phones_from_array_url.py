# Descrription: Скрипт получает и выводит номера телефонов из url указанных в массиве
# Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Open the URL in Chrome browser
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
urls = ['https://krisha.kz/a/show/679724184', 'https://krisha.kz/a/show/682704362', 'https://krisha.kz/a/show/682764744', 'https://krisha.kz/a/show/682457860']
current_index = 0 # Изначальная положение индекса в массиве начинается с 0

while True:
    driver.get(urls[current_index])
    current_index += 1 # Инкрементация положения указателя в массиве на 1 вперед

    # Click on the 'show phones' button and wait for the phone number to appear
    show_phones_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'show-phones')))
    show_phones_button.click()

    # Wait 10 seconds untill element class 'offer__contects-phones' will visible
    phone_number = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'offer__contacts-phones')))

    # Get the phone number text from the element
    number = phone_number.text.strip()

    # Print the phone number
    print(number)

    # Код, чтобы не выйти за пределы массива
    if current_index >= len(urls):
        driver.quit() # Close the browser window

    # Ждем некоторое время перед обработкой следующего URL
    time.sleep(5)