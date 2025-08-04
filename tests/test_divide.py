from src.utils import divide
def test_divide():
    a = 6
    b = 2
    expected = 3

    assert divide(a, b) == 3, f"Expected {expected}, but got {divide(a, b)}"
