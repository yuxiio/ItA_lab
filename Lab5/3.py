
# def f_recursion(n,l,r):
#     if(r<L or l > R):
#         return 0
#     if(n < 2):
#         if(l>=L and r<=R):
#             return n
#         else:
#             return 0
#     mid = (l+r)//2
#     return f_recursion(n//2,l,mid-1)+f_recursion(n%2,mid,mid)+f_recursion(n//2,mid+1,r)

# global N,L,R 
# N,L,R  = map(int,input().split())
# lengh,i,temp = 0,0,N
# while(temp >= 1):
#     lengh+=2**i
#     i+=1
#     temp = temp //2
# print(f_recursion(N,1,lengh))



"""
Created on Wed Feb 22 20:11:58 2017
 
Name: MD. Khairul Basar
Phone: 01760446942
Email: khairul.basar93@gmail.com
"""
 
# def bit_length(x):
    
#     ans = 0;
#     while(x):
#         ans+=1;
#         x = x//2;
#     return max(ans,1);

def get_digits_bit(n):
    if n==1 or n==0:
        return 1
    digits = 0
    while(n):
        digits += 1
        n //= 2
    return digits
 
def f_recursion(x,pos,size,l,r):
    
    if(x <= 1):
        return x
    
    ans = 0
    if(l < pos):
        ans+=f_recursion(x//2,pos-size,size//2,l,r)
    if(pos>=l and pos<=r):
        ans+=x%2
    if(r > pos):
        ans+=f_recursion(x//2,pos+size,size//2,l,r)
 
    return ans
 
n,l,r = map(int,input().split())
length = get_digits_bit(n)
x = 1<<(length-1)
ans = f_recursion(n,x,x//2,l,r)
print(ans)