
class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
    def show(self):
        print(f"Student: {self.name}")
        print(f"Course: {self.course}")

student = Student("Tommi", "Master IT")

student.show()
