# Вакансии

n, m = map(int, input().split())
salary_matrix = [list(map(int, input().split())) for _ in range(n)]

# отслеж занятых вакансий и кандидатов
vacancies_filled = [False] * n
candidates_assigned = [False] * m

total_salary = 0

# пока будут незанятые вакансии и кандидаты
while True:
    min_salary = float('inf')
    min_i, min_j = -1, -1
    
    # проверяем минимальную зарплату, которая не занята
    for i in range(n):
        if not vacancies_filled[i]:  # если вакансия еще не занята
            for j in range(m):
                if not candidates_assigned[j]:  # если кандидат еще не назначен
                    if salary_matrix[i][j] < min_salary:
                        min_salary = salary_matrix[i][j]
                        min_i, min_j = i, j

    # если нет пар, т овыходм
    if min_i == -1:
        break
    
    # даем вакансию кандидату
    vacancies_filled[min_i] = True
    candidates_assigned[min_j] = True
    total_salary += min_salary

print(total_salary)
