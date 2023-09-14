message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r" # що потрібно порахувати
result = 0 # Початкове значення для лічильника
# Використовуємо цикл for для ітерації кожного символу у рядку message
for char in message:
    if char == search:
        result += 1 # Якщо знайдено символ search, збільшуємо result на 1

print (f"Кількість входжень символу '{search}' у рядку: {result}")