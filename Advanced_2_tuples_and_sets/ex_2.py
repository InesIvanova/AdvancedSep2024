n = int(input())

students = {}

for _ in range(n):
    data = tuple(input().split())
    name, grade = data
    grade = float(grade)

    if name not in students:
        students[name] = []
    students[name].append(grade)

for student_name, grades in students.items():
    avg_grade = sum(grades) / len(grades)
    print(f"{student_name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg_grade:.2f})")