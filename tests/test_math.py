import pytest

def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


# Multiplication test ideas:
# two positive integers
# identity: multiplying by 1
# zero: multiply by 0
# positive by a negative
# negative by a negative
# multiply floats
#
# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6
#
# def test_multiply_identity():
#     assert 1 * 99 == 99
#
# def test_multiply_zero():
#     assert 0 * 100 == 0
#
# # DRY Principle: Don't Repeat Yourself!

products = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
