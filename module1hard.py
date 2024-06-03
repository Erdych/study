average_grades = {

}
grades = [
    [5, 3, 3, 5, 4],
    [2, 2, 2, 3],
    [4, 5, 5, 2],
    [4, 4, 3],
    [5, 5, 5, 4, 5]
]
students = {
    'Johnny',
    'Bilbo',
    'Steve',
    'Khendrik',
    'Aaron'
}
student_list = sorted(students)
for i in range(0, len(student_list)):
    average_grades.update({student_list[0] : sum(grades[0]) / len(grades[0])})
    student_list.remove(student_list[0])
    grades.remove(grades[0])
    
print(average_grades)
