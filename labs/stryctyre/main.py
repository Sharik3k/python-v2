from models import Medicine, Antibiotic, Vitamin, Vaccine
from typing import List

def print_medicine_details(medicines: List[Medicine]):
    """
    Приймає список будь-яких об'єктів-спадкоємців Medicine
    і друкує їхню інформацію, не перевіряючи конкретний тип.
    """
    print(" Інформація про медикаменти на складі \n")
    for med in medicines:
        print(med.info())
        print("-" * 25)

if __name__ == "__main__":
    # 1. Створення списку з різними типами медикаментів
    pharmacy_stock = [
        Antibiotic(name="Амоксицилін", quantity=50, price=120.50),
        Vitamin(name="Вітамін C", quantity=200, price=85.00),
        Vaccine(name="Вакцина від грипу", quantity=15, price=350.00)
    ]

    # 2. Виклик єдиної функції для обробки всього списку
    print_medicine_details(pharmacy_stock)
    
    # 3. Демонстрація валідації типів
    try:
        invalid_med = Vitamin(name="Неправильний", quantity="багато", price=99)
    except TypeError as e:
        print(f"\nПомилка створення об'єкта: {e}")