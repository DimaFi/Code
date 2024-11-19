def sort_students_by_average(filename):
    students = []
    
    with open(filename, 'r') as file:
        N = int(file.readline().strip()) 
        for _ in range(N):
            line = file.readline().strip()
            parts = line.split()
            
            surname = parts[0]
            name = parts[1]
            patronymic = parts[2]
            birth_year = parts[3]
            grades = list(map(int, parts[4:]))
            
            average = sum(grades) / len(grades)
            
            students.append((surname, name, patronymic, birth_year, grades, average))
    
    students.sort(key=lambda student: student[5])
    
    #with open(r'D:\Code\Vault\Machine\4.1 Сортировки\4.1_1\sorted_students.txt', 'w') as file:
    with open('sorted_students.txt', 'w') as file:
        for student in students:
            line = f"{student[0]} {student[1]} {student[2]} {student[3]} " + " ".join(map(str, student[4]))
            file.write(line + '\n')

#sort_students_by_average(r'D:\Code\Vault\Machine\4.1 Сортировки\4.1_1\students.txt')
sort_students_by_average('students.txt')
