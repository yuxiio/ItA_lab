for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
 
    cnt = best = s[:k].count('W')
    for i in range(k,n):
        cnt -=  (s[i-k]=="W")-(s[i]=="W")
        best = min(best, cnt)
    print(best)