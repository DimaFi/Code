import numpy as np

n, m = map(int, input().split())
salary_matrix = np.array([list(map(int, input().split())) for _ in range(n)])


vacancies_filled = np.zeros(n, dtype=bool)
candidates_assigned = np.zeros(m, dtype=bool)

total_salary = 0

while True:
    # маска вакансий
    mask = ~vacancies_filled[:, None] & ~candidates_assigned[None, :]

    if not mask.any():
        break

    # самая мин зп
    min_index = np.unravel_index(np.argmin(np.where(mask, salary_matrix, np.inf)), salary_matrix.shape)
    min_salary = salary_matrix[min_index]

    # ставим кандандита на вакансию
    vacancies_filled[min_index[0]] = True
    candidates_assigned[min_index[1]] = True

    total_salary += min_salary

print(total_salary)
