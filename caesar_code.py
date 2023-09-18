message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
            # Визначаємо базовий зсув для великих і малих літер
        if ch.islower():
            pos = ord('a')
        else:
            pos = ord('A')
            
            # Обчислюємо новий символ з урахуванням зсуву
        offset_ch = chr(((ord(ch) - pos + offset) % 26) + pos)
        encoded_message += offset_ch
    else:
        # Якщо символ не є буквою, додаємо його без змін
        encoded_message += ch
print(f"Закодована фраза: {encoded_message}")