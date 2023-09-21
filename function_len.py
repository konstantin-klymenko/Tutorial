'''Створіть функцію format_string для форматування рядка. У функцію ми передаємо рядок string та length довжину нового рядка.
 Функція повертає новий рядок за наступним алгоритмом:

Якщо довжина вихідного рядка більша або дорівнює length, ми повертаємо його в тому ж вигляді;
Якщо вона менша length, ми додаємо попереду рядка пробіли в кількості (length - len(string)) // 2.'''

def format_string(string, length):
   if len(string) >= length:
       print (len(string))
       return string

   elif len(string) < length:
       left_space = (length - len(string)) // 2
       return ' ' * left_space + string
   

print (format_string("strin", 6))

# string = 'Hello'
# print (len(string))