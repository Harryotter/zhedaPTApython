#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
import math
n=int(input())
a=[]
for k in range(n):
    a.append(int(input()))
def prime(num):
    if num<2:
        return False
    else:
        for j in range(2,int(math.sqrt(num+1))):
            if num%j==0:
                return False
        else:
            return True
for i in range(n):
    if prime(a[i]):
        print("Yes")
    else:
        print("No")
# 本题需要注意一下判断素数的函数中，为防止爆栈采取根号的范围时，要将结果设为整型