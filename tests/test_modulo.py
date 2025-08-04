from src.utils import modulo

def test_modulo():
    a = 2
    b = 3
    expected = 2

    result = modulo(a, b)

    assert result == 2, f"Expected {expected}, got {result}" 


