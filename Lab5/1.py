import sys
n,l,r = map(int,input().split())
# n,l,r = 1 , 1 , 1


numbers = 0
num_base = 0
arr = []
digits = 0
memorandum = {}

def f_special_sequence(n):
    global memorandum
    global num_base
    global digits
    if n<8:
        num_base = n//2
        digits += 2
        return [n&1]
    m = n//2
    digits += 1
    if (m) in memorandum:
        return memorandum[m] + [n&1] + memorandum[m]
    else:
        memorandum[m] = f_special_sequence(n//2)
        return memorandum[m] + [n&1] + memorandum[m]
    # return f_special_sequence(n//2) + [n&1] + f_special_sequence(n//2)

arr = f_special_sequence(n)
num_base_outside = num_base // 2
num_base_middle = num_base & 1
num_base_count = num_base_middle + num_base_outside*2

# print(arr,num_base,num_base_middle,num_base_outside,digits)
def return_num(c):
    global num_base_middle
    global num_base_outside
    if c==1:return num_base_outside
    if c==2:return num_base_middle + num_base_outside
    if c==3:return num_base_middle + num_base_outside*2
    if c==0:return 0

def get_num(a,b):
    global num_base_middle
    global num_base_outside
    s = 0
    if a==b:
        if a==1 or a==3:return num_base_outside
        if a==2:return num_base_middle
    else:
        for u in range(a,b+1):
            if u==1 or u==3:
                s += num_base_outside
            if u==2:
                s += num_base_middle
        return s


left_digit = 0
right_digit = 0
i = 0
is_find_left = False
is_find_right = False
while (not is_find_left) or (not is_find_right):
    if 3 >= i-l >= 0:
        numbers += return_num(i-l)
        left_digit = i//4
        is_find_left = True
    if 3 >= r-i >= 0:
        numbers += return_num(r-i)
        right_digit = i//4
        is_find_right = True
    i = i + 4
if right_digit-left_digit > 0 :
    numbers += (right_digit-left_digit) * num_base_count
if right_digit-left_digit < 0 :
    numbers = 0
    numbers += get_num(l-4*(left_digit-1),r-right_digit*4)


numbers += arr[left_digit-1:right_digit].count(1)

if n<2:
    print(n)
else:
    print(numbers)
