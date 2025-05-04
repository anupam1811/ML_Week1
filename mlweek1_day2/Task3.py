students = {1: "Anuj Dwivedi", 2: "Anupam Shukla", 3: "Vishal Prajapati"}

def search_student(roll_number):
    return students.get(roll_number, "Student not found")

roll_number = int(input("Enter roll number: "))
print(search_student(roll_number))