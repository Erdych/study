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
students_sorted = list(students)
# Создана переменная, которая хранит список с именами студентов, необходимая для следующей операции
students_sorted.sort() 
# Теперь список сортирован в алфавитном порядке
# Каждый элемент принял порядковый номер, совпадающий с индексом соответствующего ему элемента из списка оценок (grades)

average_grades.update(
        {
            students_sorted[0] : sum(grades[0]) / len(grades[0]), 
            students_sorted[1] : sum(grades[1]) / len(grades[1]),
            students_sorted[2] : sum(grades[2]) / len(grades[2]),
            students_sorted[3] : sum(grades[3]) / len(grades[3]),
            students_sorted[4] : sum(grades[4]) / len(grades[4])
        }  
    )
# sum(grades[x]) / len(grades[x]) # Формула для нахождения среднего балла

print(average_grades)