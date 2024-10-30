def main():
    s = input()
    rep = ['a', 'e', 'i', 'o', 'u']
    s = 'C' + s
    s1 = ['C']
    for i in range(1, len(s)):
        if s[i] == 'y':
            if s1[i-1] == 'C':
                s1 += 'V'
            else:
                s1 += 'C'
        else:
            if s[i] in rep:
                s1 += 'V'
            else:
                s1 += 'C'

    print(*s1[1:],sep='')


main()
