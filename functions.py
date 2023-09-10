def ages():
    age = input("How old are you? ")
    try:
        age = int(age)
        if age >= 18:
            print("You are adult.")
        else:
            print("You are infant")
    except ValueError:
        print(f"{age} is not a number")

def name_data():
    first_name = input("Type your name? ")
    last_name = input("Type your soname? ")
    print(f'Hello dear {first_name}!')

name_data()
ages()


