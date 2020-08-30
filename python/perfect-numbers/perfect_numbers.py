def divisorGenerator(n: int):
    large_divisors = []
    for i in range(1, int(n ** 0.5 + 1)):  # From 1 to sqrt(n) + 1
        if n % i == 0:
            yield i
            if i * i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield int(divisor)


def classify(number):
    if number < 1:
        raise ValueError("Error")
    a = sum(list(divisorGenerator(number))[:-1])
    if a == number:
        return "perfect"
    elif a < number:
        return "deficient"
    else:
        return "abundant"
