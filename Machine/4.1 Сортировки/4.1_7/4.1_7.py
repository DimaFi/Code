with open('input.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0].strip())

excluded_firm = lines[-1].strip() # исключить фирму

supplies = []
for line in lines[1:n+1]: 
    name, firm, quantity = line.rsplit(' ', 2)
    supplies.append((name, firm, int(quantity)))

# исключаем поставки той фирмы
filtered_supplies = [supply for supply in supplies if supply[1] != excluded_firm]

# Сортируем данные:
# 1. По названию
# 2. По количеству товара в порядке убывания
# 3. При совпадении наименования и количества — сохраняем исходный порядок
sorted_supplies = sorted(filtered_supplies, key=lambda x: (x[0], -x[2]))

# берем первеы 10 строк
result = sorted_supplies[:10]

with open('output.txt', 'w') as file:
    for name, firm, quantity in result:
        file.write(f"{name} {firm} {quantity}\n")
