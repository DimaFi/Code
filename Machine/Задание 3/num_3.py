import csv

with open('task19.csv', 'r', encoding='cp1251') as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)  # пропускаем заголовок
    data = [[item.strip() for item in row] for row in reader if len(row) >= 6]
    # for row in reader:
    #     print(row)
    print(data)

for row in data:
    print(row)

# 1: На какое суммарное расстояние были произведены перевозки с 7 по 9 октября?
distance = sum(int(row[3]) for row in data if '7 октября' <= row[0] <= '9 октября')

# 2: Какова средняя масса груза при автоперевозках, осуществлённых из города Осинки? 
osinki = [int(row[5]) for row in data if row[1] == 'Осинки']
avg = sum(osinki) / len(osinki) if osinki else 0

# 3: Какой суммарный расход бензина был при осуществлении перевозок с 1 по 3 октября? 
fuel = sum(int(row[4]) for row in data if '1 октября' <= row[0] <= '3 октября')

# 4: Какова средняя масса груза при автоперевозках, осуществлённых в город Березки? 
berezki = [int(row[5]) for row in data if row[2] == 'Березки']
avg2 = sum(berezki) / len(berezki) if berezki else 0

print(f"Суммарное расстояние с 7 по 9 октября: {distance} км")
print(f"Средняя масса груза из города Осинки: {avg:.2f} кг")
print(f"Суммарный расход бензина с 1 по 3 октября: {fuel} л")
print(f"Средняя масса груза в город Березки: {avg2:.2f} кг")
