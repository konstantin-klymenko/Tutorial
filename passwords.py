from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 7:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    if len(password) != 8:
        return False

    has_upper = False
    has_lower = False
    has_num = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_num = True

    return has_upper and has_lower and has_num


def get_password():
    max_attempts = 100  # Максимальна кількість спроб генерації пароля
    attempts = 0  # Лічильник спроб

    while attempts < max_attempts:
        password = get_random_password()  # Генеруємо випадковий пароль
        if is_valid_password(password):  # Перевіряємо його на надійність
            return password  # Повертаємо надійний пароль
        attempts += 1

    return attempts

www = get_password()
print (www)