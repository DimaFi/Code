k = int(input())

if 11 <= k % 100 <= 19:
    print(f"Мне {k} лет")
else:
    if k % 10 == 1:
        print(f"Мне {k} год")
    elif 2 <= k % 10 <= 4:
        print(f"Мне {k} года")
    else:
        print(f"Мне {k} лет")
