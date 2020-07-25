#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
import math
n=int(input())
res=1
for i in range(1,n+1):
    res=res+1/math.factorial(i)
print("{:.8f}".format(res))
# 使用递归时，最大测试点1000会爆栈，要使用递推写或者使用自带函数
# math.factorial()