import pytest
from pytest import approx

from moneyclean.service_body_test import Order

# --- Фікстури ---

@pytest.fixture
def empty_order():
    return Order(id=100, items=[])

@pytest.fixture
def simple_order():
    items = [{'price': 10.0, 'quantity': 2}]
    return Order(id=101, items=items)

@pytest.fixture
def complex_order():
    items = [
        {'price': 10.0, 'quantity': 2},
        {'price': 50.0, 'quantity': 1},
        {'price': 5.5, 'quantity': 10}
    ]
    return Order(id=102, items=items)

# --- total() ---

def test_total_empty(empty_order):
    assert empty_order.total() == 0

def test_total_simple(simple_order):
    assert simple_order.total() == 20.0

def test_total_complex(complex_order):
    assert complex_order.total() == 125.0

def test_total_with_zero_quantity():
    order = Order(id=103, items=[
        {'price': 100.0, 'quantity': 1},
        {'price': 1000.0, 'quantity': 0}
    ])
    assert order.total() == 100.0

# --- most_expensive() ---

def test_most_expensive_simple(simple_order):
    assert simple_order.most_expensive() == {'price': 10.0, 'quantity': 2}

def test_most_expensive_complex(complex_order):
    assert complex_order.most_expensive() == {'price': 50.0, 'quantity': 1}

# --- apply_discount() ---

def test_apply_discount_valid(complex_order):
    complex_order.apply_discount(20)
    expected_prices = [8.0, 40.0, 4.4]
    actual_prices = [item['price'] for item in complex_order.items]

    assert actual_prices == approx(expected_prices)
    assert complex_order.total() == approx(100.0)

def test_apply_discount_zero(simple_order):
    original_price = simple_order.items[0]['price']
    simple_order.apply_discount(0)
    assert simple_order.items[0]['price'] == original_price

def test_apply_discount_full(simple_order):
    simple_order.apply_discount(100)
    assert simple_order.items[0]['price'] == 0.0
    assert simple_order.total() == 0.0

def test_apply_discount_invalid_negative(simple_order):
    with pytest.raises(ValueError, match="Invalid discount"):
        simple_order.apply_discount(-10)

def test_apply_discount_invalid_over_100(simple_order):
    with pytest.raises(ValueError, match="Invalid discount"):
        simple_order.apply_discount(101)

# --- repr() ---

def test_repr_simple(simple_order):
    assert repr(simple_order) == "<Order 101: 1 items>"

def test_repr_empty(empty_order):
    assert repr(empty_order) == "<Order 100: 0 items>"
