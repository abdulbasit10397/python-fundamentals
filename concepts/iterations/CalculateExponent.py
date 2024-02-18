def calculate_exponent(num, power):
    exponent = 1
    for index in range(power):
        exponent *= num

    return exponent


print(calculate_exponent(7, 4))
