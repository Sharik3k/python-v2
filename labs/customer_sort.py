clients = [
    {"ім’я": "Іван", "сума угоди": 50, "статус перевірки": "clean"},
    {"ім’я": "Марія", "сума угоди": 500, "статус перевірки": "suspicious"},
    {"ім’я": "Олег", "сума угоди": 50, "статус перевірки": "fraud"},
    {"ім’я": "Анна", "сума угоди": 1000, "статус перевірки": "clean"},
    {"ім’я": "Сергій", "сума угоди": 500, "статус перевірки": "unknown"},
]

results = []

for client in clients:
    name = client.get("ім’я")
    amount = client.get("сума угоди")
    status = client.get("статус перевірки")

    
    if not isinstance(amount, (int, float)):
        results.append(f"{name}: Фальшиві дані")
        continue

    
    if amount < 100:
        category = "Дрібнота"
    elif amount < 1000:
        category = "Середнячок"
    else:
        category = "Великий клієнт"


    match status:
        case "clean":
            decision = "Працюває без питань"
        case "suspicious":
            decision = "Перевірити документи"
        case "fraud":
            decision = "У чорний список"
        case _:
            decision = "Невідомий статус"

    results.append(f"{name}: {category}, {decision}")


for r in results:
    print(r)
