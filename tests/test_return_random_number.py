from src.utils import return_random_number
def test_return_random_number():
    ''' 
    The unit test checks that the random number is between 0 and 100.
    '''
    assert 0 <= return_random_number() <= 100