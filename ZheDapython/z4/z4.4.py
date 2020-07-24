#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
import math
n=int(input())
def is_primer(num):
    if num>1:
        for j in range(2,int(math.sqrt(num))+1):
            if num%j==0:
                return False
        else:
            return True
    else:
        return False
for y in range(2,n):
    x=n-y
    if is_primer(y) and is_primer(x):
        print("{} = {} + {}".format(n,y,x))
        break
# 判断素数若不用根号则会运行超时
# "N = p + q"N的素数分解中，p按最小分解则是q按最大分解即是选择p顺序输出,q取补数