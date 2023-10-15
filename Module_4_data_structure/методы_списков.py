def prepare_data(data):
    if len(data) < 3:
        # Якщо у списку менше 3 елементів, то неможливо видалити найбільше та найменше значення
        return data
    
    # Видаляємо найбільше і найменше значення
    data.remove(max(data))
    data.remove(min(data))
    
    # Сортуємо список в порядку зростання
    data.sort()
    
    return data

# Приклад використання
data = [5, 2, 8, 1, 9, 3]
prepared_data = prepare_data(data)
print(prepared_data) 