import sys
sys.setrecursionlimit(2005000)

def get_info(arr):
    is_exist = {}
    info = {}
    for i in range(len(arr)):
        info[i] = {'left':float('-inf'),
                    'right':float('inf')}
        if arr[i] in is_exist:
            info[i]['left'] = is_exist[arr[i]]
            info[is_exist[arr[i]]]['right'] = i
        is_exist[arr[i]] = i
    return info



def is_unique_point(start,end,index):
    global dic
    if dic[index]['left'] < start and dic[index]['right'] > end:
        return True
    else:
        return False

# {1:{"left":1,"right":3},2:{"left":1,"right":3}}


# 1 2 3 2 1 2

# -inf 4
# -inf 3
# -inf inf
# 1 5
# 0 inf
# 3 inf



def is_non_boring(start,end):
    r = start
    l = end
    if start >= end:return True
    while r <= l:
        if(is_unique_point(start,end,r)):
            return is_non_boring(start,r-1) and is_non_boring(r+1,end)
        if(is_unique_point(start,end,l)):
            return is_non_boring(start,l-1) and is_non_boring(l+1,end)  
        r += 1
        l -= 1  
    return False
    



t = int(input())

while t > 0:
    t -= 1
    n = int(input())
    arr = list(map(int,input().split()))
    dic = get_info(arr)
    if is_non_boring(0,len(arr)-1):
        print("non-boring")
    else:
        print("boring")
    

