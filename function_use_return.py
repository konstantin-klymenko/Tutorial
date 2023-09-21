def invite_to_event(username):
    return f"Dear {username}, we have the honour to invite you to our event."

# Приклад використання функції:
invite_message = invite_to_event("John")
print(invite_message)

def add_ten(a):
    b = 10
    return a + b

print(add_ten(10))

""" Необхідно реалізувати функцію розрахунку ціни товару зі знижкою discount_price. 
Функція приймає ціну price та знижку discount — це дрібне число від 0 до 1. 
Тут і надалі ми під знижкою розумітимемо коефіцієнт, який визначає розмір від ціни. 
І на цей розмір ми знижуємо підсумкову вартість товару. Логіку функції необхідно прописати у внутрішній функції apply_discount, 
використовуючи оголошення зміною price як nonlocal."""

def discount_price(price, discount):
    price_with = price - (price * discount)
    return price_with
    

print(discount_price(100, 0.3))