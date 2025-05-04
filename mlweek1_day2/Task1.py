marks = [[80, 90, 70], [90, 85, 95],[75, 80, 85]]

for i, student_marks in enumerate(marks):
    total = sum(student_marks)
    average = total / len(student_marks)
    print(f"Student {i+1} Total: {total}, Average: {average:.2f}")