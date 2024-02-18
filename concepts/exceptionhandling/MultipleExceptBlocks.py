try:
    value = 10 / 0
    number = int(input("Enter your number: "))
    print(number)

except ZeroDivisionError:
    print("Zero Division Error")
except ValueError:
    print("Invalid number provided")
