import re

text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net \
      +380(67)111-777-777+380(67)777-77-787'

def find_all_phones(text):
    # Регулярний вираз для пошуку телефонних номерів
    pattern1 = r'\+\d{3}\(\d{2}\)\d{3}-\d{2}-\d{2}'
    pattern2 = r'\+\d{3}\(\d{2}\)\d{3}-\d{1}-\d{3}'
    # Знаходимо всі телефонні номери в тексті
    phones1 = re.findall(pattern1, text)
    phones2 = re.findall(pattern2, text)
    
    # Об'єднуємо два списки в один
    all_phones = phones1 + phones2
    
    return all_phones

res = find_all_phones(text)
print(res)
