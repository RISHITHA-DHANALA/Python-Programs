student = {}

student["name"] = input("Enter name: ")
student["roll"] = input("Enter roll number: ")
student["marks"] = input("Enter marks: ")

print("\nStudent Details:")
for key, value in student.items():
    print(key.capitalize(), ":", value)
