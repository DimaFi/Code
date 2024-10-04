n = int(input())
sum = 0


for i in range(n):
    sum += int(input())

m = int(input())

if sum <= m:
    print("True")
else:
    print("False")