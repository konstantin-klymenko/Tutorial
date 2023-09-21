def print_max(a, b):
    if a > b:
        print(a, 'максимально')
    elif a == b:
        print(a, 'дорівнює', b)
    else:
        print(b, 'максимально')

print_max(3, 4)  # пряма передача значень

x = 5
y = 7
print_max(x, y)  # передача змінних у якості аргументів

"""Напишімо функцію, яка повертає повне ім'я користувача. 
У базі даних переважно зберігають ім'я користувача first_name, 
його прізвище last_name та по батькові, або, як заведено в західних країнах, 
друге ім'я — middle_name. Причому middle_name — це необов'язкова змінна, 
вона може бути, а може й не передаватися під час виклику функції. 
Наша функція повертатиме рядок з повним ім'ям 'first_name middle_name last_name', 
якщо ж змінна middle_name відсутня, то рядок, що повертається повинен бути 'first_name last_name'."""
def get_fullname(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

# Приклади використання функції:
full_name_1 = get_fullname("John", "Doe")
print(full_name_1)  # Виведе: John Doe

full_name_2 = get_fullname("Alice", "Smith", "Marie")
print(full_name_2)  # Виведе: Alice Marie Smith