def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        qw = fibonacci(n - 1) + fibonacci(n - 2)
        print (qw)
        return qw
        

# Приклад використання:
n = 5  # Задане число n
result = fibonacci(n)
print(f"{n}-те число ряду Фібоначчі: {result}")




    

