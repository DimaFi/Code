def main():
    s = input()
    new_c = set()
    non_rare_c = set()

    for char in s:
        if char in new_c:
            non_rare_c.add(char)
        else:
            new_c.add(char)

    rare_letters = sorted(new_c - non_rare_c) # только те, которые есть в new, но нету в non_rare, то есть ровно 1 раз

    print(''.join(rare_letters))

main()
