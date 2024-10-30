def main():
    a, b, c = map(int, input().split())
    count = len(set([a, b, c])) # длина = кол-во действий, т.к. только уникальные в set
    print(count - 1)
    
main()
