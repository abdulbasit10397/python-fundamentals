def sum_all_numbers(numbers):
    sum = 0
    for n in numbers:
        sum += n
    print(sum)


def find(numbers, num):
    result = -1
    for n in numbers:
        if n == num:
            result = n

    if result >= 0:
        print(str(num) + " is present.")
    else:
        print(str(num) + " is not present.")


numbers = [10, 45, 32, 56, 76, 87, 98, 23, 67]

print("******* SUM ALL LIST ELEMENTS")
sum_all_numbers(numbers)

print("\n******* SEARCHING IN LIST *********")
find(numbers, 76)
