def cycle_inside_cycle():
    num = int(input("Enter integer (0 for output): "))
    sum = 0
    while num > 0:
        for i in range (0, num + 1):
            sum += i
        print (sum)
        num = int(input("Enter integer (0 for output): "))

def cycle_break():
    # Ініціалізуємо змінну sum
    sum = 0

    while True:
        num = int(input("Введіть ціле число (або 0 для виходу): "))
        
        if num == 0:
            break  # Виходимо з першого циклу, якщо введено 0
        
        # Використовуємо цикл for для обчислення суми чисел від 0 до введеного числа
        for i in range(0,num + 1):
            sum += i

    # Виводимо результат
    print(f"Загальна сума всіх введених чисел: {sum}")


def cycle_continue():
    sum = 0
    while True:
        num = int(input("Enter integer (0 for output): "))
        if num == 0:
            break
        for i in range(num + 1):
            if i % 2 == 1:
                continue
            print (i)
            sum = sum + i
        print (sum)

cycle_continue()