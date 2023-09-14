def result(a, b):
    while b:
        a, b = b, a % b
    return a

# Введення двох чисел від користувача
first = int(input("Введіть перше число: "))
second = int(input("Введіть друге число: "))

# Визначення НСД та виведення результату
gcd = result(first, second)
print(f"Найбільший спільний дільник {first} і {second} дорівнює {gcd}")