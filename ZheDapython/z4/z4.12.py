#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
fiblist=[1,1]
while fiblist[-1]<=n:
    fiblist.append(fiblist[-1]+fiblist[-2])
print(fiblist[-1])
# 本题因为循环次数的不确定性采用while循环
# 利用序列下标-1来表示序列末尾的数与输入的数比较


