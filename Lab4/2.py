# def get_info(arr):
#     is_exist = {}
#     info = {}
#     for i in range(len(arr)):
#         info[i] = {'left':float('-inf'),
#                     'right':float('inf')}
#         if arr[i] in is_exist:
#             info[i]['left'] = is_exist[arr[i]]
#             info[is_exist[arr[i]]]['right'] = i
#         is_exist[arr[i]] = i
#     return info


# print(get_info([1,1,2,1,1]))
import sys
import random
sys.setrecursionlimit(200100)
MAX_INT_NUMBER = 100000000     # 随机数范围，暂定从0~10w

# @param n      测试集规模，生成n个随机数列表

def generateTestSet_Int(n):
    list = []
    i = 0
    while i < n:
        list.append(random.randint(0,MAX_INT_NUMBER))
        i += 1
    return list

import time

# @param fun    具体排序函数指针
# @param n      测试集规模 如1e4->10000
# @param k      计算次数，用于求平均值

def returnCalculateRes_avg(fun, n, k):
    sum = 0
    i = 0
    while i < k:
        list = generateTestSet_Int(n)
        t1 = time.perf_counter_ns()
        fun(list,0,len(list)-1)
        t2 = time.perf_counter_ns()
        sum += (t2 - t1)/1e9
        i += 1
    return sum/k


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



def is_non_boring(start,end):
    r = start
    l = end
    if start >= end:return True
    while r <= l:
        # print(is_unique_point(start,end,r))
        if(is_unique_point(start,end,r)):
            return is_non_boring(start,r-1) and is_non_boring(r+1,end)
        if(is_unique_point(start,end,l)):
            return is_non_boring(start,l-1) and is_non_boring(l+1,end)  
        r += 1
        l -= 1  
    return False


t1 = time.perf_counter_ns()
arr = generateTestSet_Int(200000)
t1 = time.perf_counter_ns()
dic = get_info(arr)
is_non_boring(0,len(arr)-1)
t2 = time.perf_counter_ns()
t = (t2 - t1)/1e3

print(t)







# 1 2 3 4 5 6 7 8 9 0
# 2 3 4 5 6 7 8 9 0
# 3 4 5 6 7 8 9 0