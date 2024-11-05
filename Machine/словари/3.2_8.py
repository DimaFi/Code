
s = input().strip()

grades_count = {2: 0, 3: 0, 4: 0, 5: 0}

i = 0
while i < len(s):
    if s[i] == '0':
        grades_count[2] += 1
        i += 1
    elif s[i:i+3] == '100':
        grades_count[3] += 1
        i += 3
    elif s[i:i+3] == '101':
        grades_count[4] += 1
        i += 3
    elif s[i:i+2] == '11':
        grades_count[5] += 1
        i += 2

most_frequent_grade = max(grades_count, key=grades_count.get)

print(most_frequent_grade)
