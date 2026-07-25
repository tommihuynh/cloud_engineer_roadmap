student = input("Student name: ")
course = input("Course: ")

with open("students.txt", "a") as file:
    file.write(f"{student}, {course}\n")

print("Student saved.")
