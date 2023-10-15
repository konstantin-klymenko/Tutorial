
def format_ingredients(ingredients_list):
    if not ingredients_list:
        return ""

    if len(ingredients_list) == 1:
        return ingredients_list[0]

    formatted_ingredients = ", ".join(ingredients_list[:-1]) + " and " + ingredients_list[-1]
    return formatted_ingredients

# Приклад використання
ingredients_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
formatted_ingredients = format_ingredients(ingredients_list)
print(formatted_ingredients)
# ingredients_list = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# print(", ".join(ingredients_list[:-1]) + " and " + ingredients_list[-1])