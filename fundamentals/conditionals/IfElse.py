# The program contains code written to practice python's conditions
num1 = 30
num2 = 20

if num1 > num2:
    print("First number", num1, "is greater")
else:
    print("Second number", num2, "is greater")

print("\n----------------------------------------------------\n")

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are male and tall")
elif is_male or is_tall:
    print("You are either male or tall")
else:
    print("You are neither male nor tall")
