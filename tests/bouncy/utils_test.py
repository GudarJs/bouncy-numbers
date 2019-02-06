from bouncy.utils import is_bouncy, calculate_least_number

"""
Test if the is_bouncy function is returning True if a number is bouncy or False otherwise.
Values were taken from the problem statement.
"""
def test_is_bouncy():
    assert is_bouncy(134468) == False
    assert is_bouncy(66420) == False
    assert is_bouncy(155349) == True

"""
Test if the calculate_least_number function is returning the least number for a given proportion of bouncy numbers.
Values were taken from the problem statement
"""
def test_calculate_least_number():
    assert calculate_least_number(50) == 538
    assert calculate_least_number(90) == 21780
