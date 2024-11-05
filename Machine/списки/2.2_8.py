def main():
    n = int(input())
    a = list(map(int, input().split()))
    g = (len(a) - a[::-1].index(max(a))-1) 
    print(*(a[:min(a.index(min(a)), (len(a) - a[::-1].index(max(a)) - 1))] + a[min(a.index(min(a)), (len(a) - a[::-1].index(max(a))-1)):max(a.index(min(a)), (len(a) - a[::-1].index(max(a))-1))+1][::-1] + a[max(a.index(min(a)), (len(a) - a[::-1].index(max(a))-1))+1:]))


main()
