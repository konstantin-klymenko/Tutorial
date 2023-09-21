result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input("Введіть число або оператор (+, -, *, /, =): ")
    
    if user_input == '=':
        break
    
    try:
        num = float(user_input)
        if wait_for_number:
            operand = num
            wait_for_number = False
        else:
            print("Помилка: спочатку введіть оператор.")
    except ValueError:
        if operator is not None and not wait_for_number:
            print("Помилка: спочатку введіть число.")
        elif user_input in ('+', '-', '*', '/'):
            if operator is not None:
                print("Помилка: оператор вже введений.")
            else:
                operator = user_input
                wait_for_number = True
        else:
            print("Помилка: невідомий оператор.")

    if not wait_for_number and operator is not None:
        if operator == '+':
            result = operand + num
        elif operator == '-':
            result = operand - num
        elif operator == '*':
            result = operand * num
        elif operator == '/':
            if num == 0:
                print("Помилка: ділення на нуль.")
            else:
                result = operand / num

# Виводимо результат
if result is not None:
    print("Результат обчислення:", result)
else:
    print("Програма завершилася без обчислень.")