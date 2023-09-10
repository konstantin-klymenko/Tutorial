x = 50

def func():
    global x 
    print('Значення x складає', x)

func()



def func():
    x = 2
    print('Змінюємо глобальне значення x на', x)

func()