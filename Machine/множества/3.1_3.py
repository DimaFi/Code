def main():
    s = input()
    new_c = set()
    non_rare_c = set()

    for char in s:
        if char in new_c:
            non_rare_c.add(char)
        else:
            new_c.add(char)

    rare_letters = sorted(new_c - non_rare_c)

    print(''.join(rare_letters))

main()
