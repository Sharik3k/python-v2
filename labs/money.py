def shadow(limit=200):
    """
    Декоратор, який перехоплює події генератора,
    рахує суму транзакцій і повідомляє, якщо ліміт перевищено.
    """
    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            total = 0
            limit_exceeded = False

            for event in gen_func(*args, **kwargs):
                print(f"→ {event}")

                # Розбиття рядка
                parts = event.split()
                if len(parts) != 2:
                    continue

                action, amount = parts

                # Перевірка валідності
                if not action.isalpha() or not amount.isdigit():
                    continue

                # Додавання до суми
                total += int(amount)

                # Перевищення ліміту
                if total > limit and not limit_exceeded:
                    print("⚠️  Тіньовий ліміт перевищено. Активую схему.")
                    limit_exceeded = True

                yield event  # просто повертаємо елемент

            print(f"💰 Фінальна сума всіх транзакцій: {total}")
        return wrapper
    return decorator


@shadow(limit=200)
def transaction_stream():
    """Генератор транзакцій."""
    transactions = [
        "payment 120",
        "refund 50",
        "transfer 90",
        "invalid_data",
        "refund x50",
        "transfer 300",
    ]
    for t in transactions:
        yield t


# Запуск
for _ in transaction_stream():
    pass