arr = []
memorandum = {}
digits = 0
count = 0

find_right = False

def f_get_base(n):
    global num_base
    global digits
    while n>8:
        n = n//2
        digits += 1
    num_base = n//2
    digits += 2
    return


middle_num = 2**(digits-1)


def f_recursion_tree(n,l,r,middle_num,digits,is_right):
    global find_right
    global count
    skip_right = False
    if (not find_right) and l > middle_num:
        skip_right = True
    if l == middle_num:
        find_right = True
    if skip_right:
        f_recursion_tree(n//2,l,r,digits-1,True)
    f_recursion_tree(n//2,l,r,digits-1,False)

# def f_recursion_tree(n,l,r,digits):
#     pan = 2**(digits-1)
#     if l==pan:
#         pass
#     elif digits==3:
#         if l < pan//2:
#             f_recursion_tree(n//2,l,r,digits-1)
#         else:
#     elif l<pan:
#         f_recursion_tree(n//2,l,r,digits-1)
#     elif l>pan:
#         f_recursion_tree(n//2,l-pan,r,digits-1)
    
        
        

# def f_special_sequence(n):
#     global memorandum
#     if n<8:
#         return [n&1]
#     m = n//2
#     if (m) in memorandum:
#         return memorandum[m] + [n&1] + memorandum[m]
#     else:
#         memorandum[m] = f_special_sequence(m)
#         return memorandum[m] + [n&1] + memorandum[m]
    

# def f_special_sequence(n):
#     global memorandum
#     if n<8:
#         return [n&1]
#     return f_special_sequence(n//2) + [n&1] + f_special_sequence(n//2)

# 903316762502 354723010040 354723105411