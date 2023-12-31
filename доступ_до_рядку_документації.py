'''Python має особливість, яка називається рядками документації, скорочено docstrings. 
Це важливий інструмент, який допомагає краще документувати програму та полегшує її розуміння. 
Рядок у першому логічному рядку функції є рядком документації для цієї функції.
Рядки документації заведено записувати у формі багаторядкового рядка, 
де перший рядок починається з великої літери та закінчується точкою. 
Другий рядок залишається порожнім, а докладний опис починається з третього. 
Рекомендується слідувати такому формату для всіх рядків документації всіх нетривіальних функцій.

Доступ до рядка документації функції можна отримати за допомогою атрибуту функції __doc__. 
Зверніть увагу на подвійне підкреслення.'''

def fun(a, b=2, c=3):
    """Знаходить суму трьох параметрів.

     Перший параметр обов'язковий, два інших за замовчанням дорівнюють 2 і 3"""
    return a + b * c


print(fun.__doc__)
print(fun(10, b=2, c=3))