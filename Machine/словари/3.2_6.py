str1 = input().strip()
str2 = input().strip()

count_str1 = {}
for char in str1:
    count_str1[char] = count_str1.get(char, 0) + 1

count_str2 = {}
for char in str2:
    count_str2[char] = count_str2.get(char, 0) + 1

result = True
for char, count in count_str2.items():
    if count_str1.get(char, 0) < count:
        result = False
        break

print(result)
