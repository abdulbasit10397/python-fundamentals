def find(numbers, num):
    result = -1
    for n in numbers:
        if n == num:
            result = n

    return result


numbers = [10, 45, 32, 56, 76, 87, 98, 23, 67]
print("\n******* SEARCHING IN LIST *********")
num = 76
result = find(numbers, num)
if result >= 0:
    print(str(num) + " is present.")
else:
    print(str(num) + " is not present.")
