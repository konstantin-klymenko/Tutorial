def positive_negative():
    
    num = int(input("Введіть число: "))
    if num > 0:
        if num >= 100:
            result = "Додатне більше 100"
        else:
            result = "Додатне менше 100"
    elif num < 0:
        result = "Число від'ємне"
    else:
        result = "Це ноль"

    print(result)

def odd_even():

    num = int(input("Enter a number: "))
    if num > 0:
        if num % 2 == 1:
            result = "Positive odd number"
        else:
            result = "Positive even number"
    elif num < 0:
        result = "Negative number"
    else:
        result = "It is zero"
        
    print(result)

positive_negative()
odd_even()
