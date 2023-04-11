def find_max_len_subarray(arr, target_sum):
    left, right = 0,0
    sum = 0
    maxlen=1000000
    key=0
    while right < len(arr):
        sum += 1
        if arr[right] == 0:
            key += 1
        # maxlen=maxlen+arr[right]
        # key=maxlen
        # maxlenlist=[]
        # maxlen1=0
        # for i in range(target_sum):
        #     maxlen1=arr[i]+maxlen1
        #     maxlenlist.append(maxlen1) 
        while sum >= target_sum:
            maxlen = min(maxlen, key)
            sum -= 1
            # maxlen=maxlen-arr[left]
            if arr[left] == 0:
                key -= 1
            left += 1    
        right += 1
    # sorted(maxlenlist)
    # x=maxlenlist[-1]
    # flist.append(target_sum-x)
    flist.append(maxlen)
a=int(input())
flist=[]
for i in range (a):
    n,k=map(int,input().split())
    testlist=[str(x) for x in input()]
    list=[]
    j=0
    while j<n:
        if testlist[j]=='B':
            list.append(1)
        else:
            list.append(0)
        j=j+1
    find_max_len_subarray(list,k)
for c in range(a):
    print(flist[c])