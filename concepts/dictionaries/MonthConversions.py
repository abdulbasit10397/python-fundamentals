month_conversions = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}

print("\n------- Getting Value by Key ---------\n")
print(month_conversions.get("1"))
print(month_conversions["2"])
print(month_conversions.get("Abuary"))
print(month_conversions.get("Abuary", "Not a Valid Key"))


print("\n------- Printing All Values in Dictionary ---------\n")
for key in month_conversions:
    print(month_conversions.get(key))
