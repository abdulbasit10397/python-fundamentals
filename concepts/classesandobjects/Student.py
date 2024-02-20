class Student:
    def __init__(self, id, name, gpa, major, semester):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.major = major
        self.semester = semester

class StudentWithFunctions:
    def __init__(self, id, name, gpa, major, semester):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.major = major
        self.semester = semester

    def on_scholarship(self):
        return self.gpa > 3.5

