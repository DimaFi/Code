import string

s = input().strip()

clean_s= ''.join(char.upper() for char in s if char.isalpha())

if clean_s == clean_s[::-1]:
    print("Yes")
else:
    print("No")
