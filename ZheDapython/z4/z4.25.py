#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
count=0
for i in range(n):
    for j in range(n-i):
        print("{} ".format(chr(ord("A")+count)),end='')
        count+=1
    if j+i==n-1:
        print("")
# 本题的思路和九九乘法表的思路类似,列的变化跟据行的变化来走