def remove_parentheses(text):
    # оставить все символы которые не в скобках
    result = []
    skip = 0

    for char in text:
        if char == '(':
            skip += 1 # игнорим
        elif char == ')':
            skip -= 1  # не игнорим текст
        elif skip == 0:
            result.append(char)  # добавляем символ

    return ''.join(result)



N = int(input())
lines = [input().strip() for _ in range(N)]

processed_lines = [remove_parentheses(line) for line in lines]

print("\n".join(processed_lines))
