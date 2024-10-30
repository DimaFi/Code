
s = input()

n = len(s)

if n % 2 == 0:
    middle = n // 2
    result = s[:middle-1] + s[middle+1:]
else:
    middle = n // 2
    result = s[:middle] + s[middle+1:]

print(result)