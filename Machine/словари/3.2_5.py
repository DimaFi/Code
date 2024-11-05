text = ""
while True:
    line = input().strip()
    text += line + " "
    if line.endswith("."):
        break

text = text.lower()

count_dict = {}

for char in text:
    if char.isalpha(): # проверка на букву
    
        count_dict[char] = count_dict.get(char, 0) + 1
    
sorted_letters = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

s = ''

for letter, count in sorted_letters:
    s += letter
    
print(s)