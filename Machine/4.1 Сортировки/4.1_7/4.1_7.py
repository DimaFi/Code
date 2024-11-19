# Чтение данных из файла
with open("input.txt", "r") as f:
    lines = f.readlines()

# Количество поставок
n = int(lines[0])

# Список поставок
supplies = [line.strip() for line in lines[1:-1]]

# Фирма, поставки которой нужно исключить
excluded_firm = lines[-1].strip()

# Фильтрация записей по фирме
filtered_supplies = [supply for supply in supplies if not supply.split()[1] == excluded_firm]

# Сортировка записей
sorted_supplies = sorted(filtered_supplies, key=lambda x: (x.split()[0], -int(x.split()[2])))

# Первые 10 записей
top_10_supplies = sorted_supplies[:10]

# Запись результата в файл
with open("output.txt", "w") as f:
    for supply in top_10_supplies:
        f.write(supply + "\n")
