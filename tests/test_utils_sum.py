from src import utils

def test_basic():
    #tests simplest case
    #Arrange
    in_a = 1
    in_b = 2
    out_expected = 3

    #Act
    out_actual = utils.sum(in_a,in_b)

    #Assert
    test_passed = out_actual == out_expected
    assert test_passed, f'utils.sum({in_a}, {in_b}) should result in {out_expected}, but got: {out_actual}'

def test_large_numbers():
    # tests large number case, no bit overflow allowed here!
    # Arrange
    in_a = 123456
    in_b = 987654
    out_expected = 1111110

    # Act
    out_actual = utils.sum(in_a, in_b)

    # Assert
    test_passed = out_actual == out_expected
    assert test_passed, f'utils.sum({in_a}, {in_b}) should result in {out_expected}, but got: {out_actual}'

