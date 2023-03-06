# To accomplish this task, we can use the requests and BeautifulSoup libraries in Python. Here's an example code:

import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/post/717962/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Указать имя класса, где лежит текс title h1
title = soup.find('h1', class_='tm-article-snippet__title tm-article-snippet__title_h1').text
print(title)


# This code sends a GET request to the URL specified in the url variable using the requests library, then uses BeautifulSoup to parse the HTML content of the page. 
# It finds the first h1 element with class post__title using the soup.find() method and extracts the text of that element using the .text attribute. 
# Finally, it prints the title using the print() function.