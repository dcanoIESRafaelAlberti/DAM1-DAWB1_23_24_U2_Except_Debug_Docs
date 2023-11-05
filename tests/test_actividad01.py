import pytest
from src.actividad01 import dividir

@pytest.mark.parametrize(
    "input_dividendo, input_divisor, expected",
    [
        (100, 4, 25),
        (7.5623, 2.356, 3.21),
        (5, 5, 1),
        (3, 2, 1.5),
        (298.563, 44.711, 6.68),
        (-88.35, 12.88, -6.86)
    ]
)
def test_dividir_params(input_dividendo, input_divisor, expected):
    assert dividir(input_dividendo, input_divisor) == expected


def test_dividir_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        dividir(1200.456, 0)