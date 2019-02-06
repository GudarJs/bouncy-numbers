def is_bouncy(number):
    list_of_digits = [int(digit) for digit in str(number)]
    digits_len = len(list_of_digits)

    last_digit = list_of_digits[0]
    increasing_count = 0
    decreasing_count = 0
    for digit in list_of_digits:
        if digit >= last_digit:
            increasing_count += 1
        if digit <= last_digit:
            decreasing_count += 1
        last_digit = digit
    is_increasing = increasing_count == digits_len
    is_decreasing = decreasing_count == digits_len

    return not is_increasing and not is_decreasing

def calculate_least_number(proportion):
    number = 0
    bouncy_numbers_count = 0
    while True:
        number += 1
        if is_bouncy(number):
            bouncy_numbers_count += 1
        calculated_proportion = bouncy_numbers_count *  100 / number
        if calculated_proportion == proportion:
            break
    return number
