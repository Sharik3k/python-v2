preparat = [
    {"назва": "Амоксил", "кількість": 20, "категорія": "antibiotic", "температура": 22.5},
    {"назва": "Вітамін C", "кількість": 50, "категорія": "vitamin", "температура": 4.0},
    {"назва": "КовіВак", "кількість": 10, "категорія": "vaccine", "температура": 26.0},
    {"назва": "Ноотропіл", "кількість": "10", "категорія": "nootropic", "температура": 21.0},
    {"назва": "БАД", "кількість": 30, "категорія": "supplement", "температура": 19.0},
    {"назва": "Гепарин", "кількість": 15, "категорія": "antibiotic", "температура": 5.0},
]

for i in preparat:
    name = i["назва"]
    quantity = i["кількість"]
    category = i["категорія"]
    temperature = i["температура"]

    if temperature < 5:
        temp = "too cold"
    elif temperature > 25:
        temp = "too hot"
    else:
        temp = "normal"

    match category:
        case "antibiotic":
            category1 = "Рецептурний препарат"
        case "vitamin":
            category1 = "Вільний продаж"
        case "vaccine":
            category1 = "Потребує спецзберігання"
        case _:
            category1 = "Невідома категорія"

    print(f"Препарат: {name}, Категорія: {category1}, Температура: {temp}")