'''Факториал — это произведение всех натуральных чисел от 1 до данного числа. 
Например, факториал числа 5 будет равен 1 × 2 × 3 × 4 × 5 = 120. 
Его используют во многих областях науки — например, комбинаторике, теории вероятностей и математическом анализе.'''

# Обчислюємо факторіал числа n за допомогою рекурсії
# @param n – число, для якого треба розрахувати факторіал
# @return - факторіал числа n
def factorial(n):
    if n < 2:
        return 1  # Базовий випадок
    else:
        return n * factorial(n - 1)  # Рекурсивний випадок


num = int(input("Введіть додатне ціле число: "))
result = factorial(num)
print(f"Факторіал числа {num} дорівнює {result}")


'''Расчет факториала--------------------------------------------------------------------------------------------------'''

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(result)
    return result

n = int(input("Введіть додатне ціле число: "))
total = factorial(n)
print (f'Факторіал числа {n} дорівнюе {total}')



'''Ми проводимо розіграш призів серед перших 50 підписників ютуб-каналу. 
Ми маємо 7 призів для розіграшу. Може виникнути питання, скільки різних списків переможців ми можемо отримати під час розіграшу? 
Для цього ми будемо використовувати формулу сполучень без повторень

Cnk = n! / ((n - k)! · k!)

де n — це загальна кількість людей (випадків), а k — кількість людей, які отримали призи.

Напишіть функцію number_of_groups, яка приймає параметри n та k, 
і за допомогою функції factorial повертає нам скільки різних списків переможців ми можемо отримати при розіграші

Зверніть увагу на те, які великі значення ми отримуємо для факторіала. 
Рекурсивні висловлювання треба завжди застосовувати з обережністю при обчисленнях, щоб не отримати переповнення пам'яті.'''

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def number_of_groups(n, k):
    if n < k:
        return 0  # Якщо кількість призів більша за загальну кількість людей, немає можливих списків переможців
    if n < 0 or k < 0:
        return 0  # Обробка недопустимих вхідних значень

    combinations = factorial(n) // (factorial(n - k) * factorial(k))
    return combinations


# Приклад використання:
n = 50  # Загальна кількість людей
k = 7   # Кількість призів
result = number_of_groups(n, k)
print(f"Кількість можливих списків переможців: {result}")