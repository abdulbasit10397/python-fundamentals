def find(matrix, key):
    for row in matrix:
        for col in row:
            if col == key:
                print(str(key) + " is found")
                return
    print(str(key) + " is not found")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [6, 7, 8]
]

find(matrix, 11)
