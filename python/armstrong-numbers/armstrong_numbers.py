def is_armstrong_number(number):
    numbers = str(number)
    exp = len(numbers)
    sum = 0
    for elem in numbers:
        sum += int(elem) ** exp
    return sum == number
