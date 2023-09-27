def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

payment = [-100, 50, -20, 30, -10]
result = amount_payment(payment)
print(f"Сума платежу наприкінці місяця: {result}")
  



    

