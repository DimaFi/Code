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

max_count = max(count_dict.values()) 
most_common_letters = [letter for letter, count in count_dict.items() if count == max_count]

result_letter = min(most_common_letters)

print(result_letter, max_count)
