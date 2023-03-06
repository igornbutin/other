# Description: Перебирает url и открывает каждый selenium, по окончанию массива закрывает webdriver
# startpage https://krisha.kz/arenda/komnaty/?das[price][to]=70000

# import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# Open the URL in Chrome browser
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
urls = ['https://krisha.kz/a/show/679724184', 'https://krisha.kz/a/show/682704362', 'https://krisha.kz/a/show/682764744', 'https://krisha.kz/a/show/682457860']
current_index = 0 # изначальная положение индекса в массиве начинается с 0

while True:
    driver.get(urls[current_index])
    current_index += 1 # инкрементация положения указателя в массиве на 1 вперед

    # код, чтобы не выйти за пределы массива
    if current_index >= len(urls):
        driver.quit() # Close the browser window

    # ждем некоторое время перед обработкой следующего URL
    time.sleep(5)