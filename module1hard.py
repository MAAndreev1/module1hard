grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = sorted(list(students))

average_grades = {}

for X in range(len(students)):
    A = sum(grades[X]) / len(grades[X])
    average_grades.update({students[X]: A})

print(average_grades)
