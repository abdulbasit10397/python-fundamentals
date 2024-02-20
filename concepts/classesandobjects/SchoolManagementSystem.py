from Student import Student
from Student import StudentWithFunctions

student1 = Student(1, "Abdul Basit", 3.5, "SE", 8)
print(student1.name)

print("\n-----------------------------------------------------\n")

student2 = StudentWithFunctions(2, "Umer Khan", 3.6, "SE", 8)
print(student2.name)
print("Scholarship Status: " + str(student2.on_scholarship()))
