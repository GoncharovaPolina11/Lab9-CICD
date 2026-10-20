import pytest

from calculator import Calculator


calculator = Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-2, 5, 3),
        (-4, -6, -10),
        (1.5, 2.5, 4.0)
    ]
)
def test_add(a, b, expected):
    result = calculator.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (5, 2, 2.5),
        (-10, 2, -5),
        (0, 5, 0)
    ]
)
def test_divide(a, b, expected):
    result = calculator.divide(a, b)
    assert result == expected


def test_divide_by_zero():

    with pytest.raises(
        ZeroDivisionError,
        match="Деление на ноль невозможно"
    ):
        calculator.divide(10, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (5, True),
        (7, True),
        (11, True),
        (4, False),
        (10, False),
        (15, False),
        (1, False),
        (0, False),
        (-5, False)
    ]
)
def test_is_prime_number(number, expected):
    result = calculator.is_prime_number(number)
    assert result == expected