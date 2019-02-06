from bouncy.utils import is_bouncy, calculate_least_number

"""
Values were taken from the problem statement
"""
def test_is_bouncy():
    assert is_bouncy(134468) == False
    assert is_bouncy(66420) == False
    assert is_bouncy(155349) == True

"""
Values were taken from the problem statement
"""
def test_calculate_least_number():
    assert calculate_least_number(50) == 538
    assert calculate_least_number(90) == 21780
