import time

urls = ["http://example.com/page1", "http://example.com/page2", "http://example.com/page3"]

for url in urls:
    # обрабатываем текущий URL
    print("Обработка URL:", url)
    
    # ждем некоторое время перед обработкой следующего URL
    time.sleep(5)