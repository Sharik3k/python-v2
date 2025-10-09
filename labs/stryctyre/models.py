from abc import ABC, abstractmethod

class Medicine(ABC):
    def __init__(self, name: str, quantity: int, price: float):
        # Перевірка типів у конструкторі
        if not isinstance(name, str) or not name:
            raise TypeError("Назва препарату має бути непорожнім рядком.")
        if not isinstance(quantity, int) or quantity < 0:
            raise TypeError("Кількість має бути цілим невід'ємним числом.")
        if not isinstance(price, (int, float)) or price < 0:
            raise TypeError("Ціна має бути невід'ємним числом.")

        self.name = name
        self.quantity = quantity
        self.price = price

    @abstractmethod
    def requires_prescription(self) -> bool:
        pass

    @abstractmethod
    def storage_requirements(self) -> str:
        pass

    def total_price(self) -> float:
        return round(self.quantity * self.price, 2)

    def info(self) -> str:
        prescription_status = "Так" if self.requires_prescription() else "Ні"
        return (
            f"   - Препарат: {self.name}\n"
            f"   - Кількість: {self.quantity} шт.\n"
            f"   - Потрібен рецепт: {prescription_status}\n"
            f"   - Умови зберігання: {self.storage_requirements()}\n"
            f"   - Загальна вартість: {self.total_price():.2f} грн"
        )

class Antibiotic(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "8–15°C, темне місце"

class Vitamin(Medicine):
    def requires_prescription(self) -> bool:
        return False

    def storage_requirements(self) -> str:
        return "15–25°C, сухово"

class Vaccine(Medicine):
    def requires_prescription(self) -> bool:
        return True

    def storage_requirements(self) -> str:
        return "2–8°C, холодильник"

    def total_price(self) -> float:
        base_price = super().total_price()
        service_charge = base_price * 0.10
        return round(base_price + service_charge, 2)