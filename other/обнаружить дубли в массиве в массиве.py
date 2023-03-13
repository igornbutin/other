# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Сайт для запуска: https://www.programiz.com/python-programming/online-compiler/

# Скрипт обнаружить дубли в массиве значений
# Подсказка #1: Не забывайте оборачивать числа в одинарные кавычки (по шаблону в автозамене ', ') или удалять нули (потом можно вернуть с помощью мультикурсора в Sublime - выделение средним колесом мыши или Ctrl+ЛКМ)
# Подсказка #2: Чтобы столбец цифр превратить в массив, используйте автозамену в Sublime

numbers = [1, 2, 3, 2, 1, 4, 5, 4, 6, 7, 8, 7, 9]

# Find duplicates using set
duplicates = set([x for x in numbers if numbers.count(x) > 1])

# Remove duplicates from the original list
numbers = list(set(numbers))

print("Original list:", numbers)
print("Duplicate numbers:", duplicates)
