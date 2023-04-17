def quick_sort(l,r,data,index):
    if l >= r:
        return
    i = l - 1
    j = r + 1
    pivot = data[(i+j) // 2][index]
    while i < j:
        while 1:
            i += 1
            if data[i][index] >= pivot:
                break
        while 1:
            j -= 1
            if data[j][index] <= pivot:
                break
        if i < j:
            data[i][index],data[j][index] = data[j][index],data[i][index]
    quick_sort(l,j,data,index)
    quick_sort(j+1,r,data,index)



t = int(input())
while t > 0:
    t -= 1
    n , m = map(int,input().split())
    arr = [list(map(int, input().split())) for _  in range(n)]
    if n==1:
        print(0)
        continue
    arr = list(zip(*arr))
    # dic = {}
    # for i in range(n):
    #     dic[i] = list(map(int,input().split()))
    ans = 0
    # for i in range(m):
    #     for k, v in enumerate(sorted(arr,key=lambda x:x[1][i],reverse=True)):
    #         ans += (n-1-k-k) * v
        # for j in range(n):
        #     ans += (n-1-j-j) * dic[j][i]
    for i in arr:
        for j, v in enumerate(sorted(i,reverse=True)):
            ans += (n-1-j-j) * v
    print(ans)


# for _ in range(int(input())):
#     n, m = map(int, input().split())
#     s = [list(map(int, input().split())) for _  in range(n)]
#     s = list(zip(*s))
#     res = 0
#     for i in s:
#         for j, v in enumerate(sorted(i)):
#             res += (n - 1 - j - j) * v
#     print(-res)
