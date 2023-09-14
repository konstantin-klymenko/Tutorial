num = int(input("Enter integer (0 for output): "))
sum = 0
while num > 0:
    for i in range (0, num + 1):
        sum += i
    print (sum)
    
        
    num = int(input("Enter integer (0 for output): "))

    '''# Ініціалізуємо змінну sum
sum = 0

while True:
    num = int(input("Введіть ціле число (або 0 для виходу): "))
    
    if num == 0:
        break  # Виходимо з першого циклу, якщо введено 0
    
    # Використовуємо цикл for для обчислення суми чисел від 0 до введеного числа
    for i in range(0,num + 1):
        sum += i

# Виводимо результат
print(f"Загальна сума всіх введених чисел: {sum}")'''