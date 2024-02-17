numbers = [10, 45, 32, 56, 76, 87, 98, 23, 67]
fruits = ["apple", "orange", "banana", "mango", "grape", "banana"]

print("\n************ Adding an item in the end ******************")
fruits.append("pomegranate")
print(fruits)

print("\n************ Removing last item ******************")
fruits.pop()
print(fruits)

print("\n************ Adding an item at a specific index  ******************")
fruits.insert(2, "Kino")
print(fruits)

print("\n************ Removing an item  ******************")
fruits.remove("Kino")
print(fruits)

print("\n************ Getting index of an item  ******************")
print(fruits.index("mango"))

print("\n************ Counting occurrence of an item  ******************")
print(fruits.count("banana"))

print("\n********** Sorting Ascending ***********")
numbers.sort()
print(numbers)

print("\n********** Sorting Descending ***********")
numbers.reverse()
print(numbers)

print("\n********** Joining 2 lists ***********")
fruits.extend(numbers)  # This will create a resultant list that's union of both fruits and numbers list
print(fruits)

