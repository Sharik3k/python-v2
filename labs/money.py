def shadow(limit=200):

    def decorator(gen_func):
        def wrapper(*args, **kwargs):
            gen = gen_func(*args, **kwargs)
            total = 0
            threshold_triggered = False

            for event in gen:
                print(f"→ {event}")

                try:
                    parts = event.split()
                    if len(parts) != 2:
                        continue

                    action, amount = parts
                    if not action.isalpha() or not amount.isdigit():
                        continue

                    amount = int(amount)
                    total += amount
                    if total > limit and not threshold_triggered:
                        print("⚠️  Тіньовий ліміт перевищено. Активую схему.")
                        threshold_triggered = True

                except Exception as e:
                    print(f"[Тіньове попередження] Некоректна транзакція: {event} ({e})")
                    continue

            print(f"💰 Фінальна сума всіх транзакцій: {total}")
            return total
        return wrapper
    return decorator


@shadow(limit=200)
def transaction_stream():
    """
    Генератор, який по черзі віддає транзакції.
    """
    transactions = [
        "payment 120",
        "refund 50",
        "transfer 90",
        "invalid_data",
        "payment notanumber",
        "transfer 300",
        "refund 40",
    ]

    for t in transactions:
        yield t


if __name__ == "__main__":
    total = transaction_stream()
