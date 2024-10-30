n = int(input())

count = 0

for _ in range(n):
    s = input()
    
    if s.count('@') == 1 and 0 < s.index('@') < len(s) - 1:
        if '..' not in s:
            count += 1

print(count)
