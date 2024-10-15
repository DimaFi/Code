s = str(input())
s1 = ''

for i in range(len(s)):
    if (i+1) % 2 == 0:
        s1 += s[i]
        

s2 = s1[::-1]

print(s2)