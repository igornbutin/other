# Description: Пример перебора элементов массива по индексу используя цикл

import time

urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]
current_index = 0

while True:
    # выбираем текущий URL и обрабатываем его
    current_url = urls[current_index]
    print("Обработка URL:", current_url)
    
    # увеличиваем индекс для выбора следующего URL
    current_index += 1
    
    # если индекс стал больше или равен длине массива, начинаем с начала
    if current_index >= len(urls):
        current_index = 0
        
    # ждем некоторое время перед обработкой следующего URL
    time.sleep(5)
    