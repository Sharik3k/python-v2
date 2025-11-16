import pytest
from pytest import approx

# Припускаємо, що ви перейменували ваш файл на 'order_manager.py'
from moneyclean.service_body_test import Order

# --- Фікстури для перевикористання тестових даних ---

@pytest.fixture
def empty_order():
    """Повертає пусте замовлення."""
    return Order(id=100, items=[])

@pytest.fixture
def simple_order():
    """Повертає просте замовлення з одним елементом."""
    # Кожен тест отримуватиме *нову* копію цього
    items = [{'price': 10.0, 'quantity': 2}]
    return Order(id=101, items=items)

@pytest.fixture
def complex_order():
    """Повертає складне замовлення з кількома елементами."""
    items = [
        {'price': 10.0, 'quantity': 2},  # total 20.0
        {'price': 50.0, 'quantity': 1},  # total 50.0
        {'price': 5.5, 'quantity': 10}   # total 55.0
    ]
    # Загальна сума: 125.0
    # Найдорожчий: {'price': 50.0, 'quantity': 1}
    return Order(id=102, items=items)

# --- Тести для методу total() ---

def test_total_empty(empty_order):
    """Перевіряє, що сума для порожнього замовлення дорівнює 0."""
    assert empty_order.total() == 0

def test_total_simple(simple_order):
    """Перевіряє коректний підрахунок для одного елемента."""
    assert simple_order.total() == 20.0  # 10.0 * 2

def test_total_complex(complex_order):
    """Перевіряє коректний підрахунок для кількох елементів."""
    assert complex_order.total() == 125.0  # (10*2) + (50*1) + (5.5*10)

def test_total_with_zero_quantity():
    """Перевіряє, що елементи з нульовою кількістю не впливають на суму."""
    items = [
        {'price': 100.0, 'quantity': 1},
        {'price': 1000.0, 'quantity': 0}
    ]
    order = Order(id=103, items=items)
    assert order.total() == 100.0

# --- Тести для методу most_expensive() ---

def test_most_expensive_empty(empty_order):
    """Перевіряє, що виклик most_expensive() на порожньому списку кидає помилку."""
    with pytest.raises(ValueError):
        empty_order.most_expensive()

def test_most_expensive_simple(simple_order):
    """Перевіряє правильне визначення для одного елемента."""
    expected_item = {'price': 10.0, 'quantity': 2}
    assert simple_order.most_expensive() == expected_item

def test_most_expensive_complex(complex_order):
    """Перевіряє правильне визначення серед кількох елементів."""
    expected_item = {'price': 50.0, 'quantity': 1}
    assert complex_order.most_expensive() == expected_item

def test_most_expensive_tie():
    """Перевіряє, що повертається перший з найдорожчих, якщо є однакові ціни."""
    items = [
        {'price': 100.0, 'quantity': 1}, # Цей має повернутися
        {'price': 50.0, 'quantity': 10},
        {'price': 100.0, 'quantity': 2}
    ]
    order = Order(id=104, items=items)
    expected_item = {'price': 100.0, 'quantity': 1}
    assert order.most_expensive() == expected_item

# --- Тести для методу apply_discount() ---

def test_apply_discount_valid(complex_order):
    """Перевіряє коректне застосування валідної знижки (20%)."""
    complex_order.apply_discount(20)
    # Очікувані нові ціни (оригінал * 0.8)
    # 10.0 -> 8.0
    # 50.0 -> 40.0
    # 5.5  -> 4.4
    expected_prices = [8.0, 40.0, 4.4]
    
    # Перевіряємо, що ціни змінилися
    actual_prices = [item['price'] for item in complex_order.items]
    
    # Використовуємо pytest.approx для надійного порівняння чисел з плаваючою комою
    assert actual_prices == approx(expected_prices)
    
    # Перевіряємо, що total() також оновився
    # (8*2) + (40*1) + (4.4*10) = 16 + 40 + 44 = 100.0
    assert complex_order.total() == approx(100.0)

def test_apply_discount_zero(simple_order):
    """Перевіряє, що знижка 0% не змінює ціну."""
    original_price = simple_order.items[0]['price']
    simple_order.apply_discount(0)
    assert simple_order.items[0]['price'] == original_price

def test_apply_discount_full(simple_order):
    """Перевіряє, що знижка 100% обнуляє ціну."""
    simple_order.apply_discount(100)
    assert simple_order.items[0]['price'] == 0.0
    assert simple_order.total() == 0.0

def test_apply_discount_invalid_negative(simple_order):
    """Перевіряє, що від'ємна знижка кидає ValueError."""
    with pytest.raises(ValueError, match="Invalid discount"):
        simple_order.apply_discount(-10)

def test_apply_discount_invalid_over_100(simple_order):
    """Перевіряє, що знижка > 100% кидає ValueError."""
    with pytest.raises(ValueError, match="Invalid discount"):
        simple_order.apply_discount(101)

def test_apply_discount_empty_order(empty_order):
    """Перевіряє, що застосування знижки до порожнього замовлення проходить без помилок."""
    try:
        empty_order.apply_discount(50)
    except Exception as e:
        pytest.fail(f"apply_discount() на порожньому замовленні несподівано кинув помилку: {e}")
    assert empty_order.total() == 0

# --- Тести для методу __repr__() ---

def test_repr_simple(simple_order):
    """Перевіряє рядок представлення для простого замовлення."""
    assert repr(simple_order) == "<Order 101: 1 items>"

def test_repr_empty(empty_order):
    """Перевіряє рядок представлення для порожнього замовлення."""
    assert repr(empty_order) == "<Order 100: 0 items>"