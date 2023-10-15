def is_valid_pin_codes(pin_codes):
    # Перевірка на порожній список
    if not pin_codes:
        return False

    # Створюємо множину для зберігання унікальних пін-кодів
    unique_pins = set()

    for pin_code in pin_codes:
        # Перевірка довжини пін-коду
        if len(pin_code) != 4:
            return False

        # Перевірка, чи всі символи в рядку - це цифри
        if not pin_code.isdigit():
            return False

        # Додаємо пін-код до множини унікальних пін-кодів
        unique_pins.add(pin_code)

    # Перевірка на дублікати
    if len(unique_pins) != len(pin_codes):
        return False

    return True

pin_codes = ['1101', '9034', '1109']
print(is_valid_pin_codes(pin_codes)) 