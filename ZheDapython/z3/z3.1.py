#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
nums=input().split()
numlist=[int(n) for n in nums]
avg=sum(numlist)/len(numlist)
for i in range(len(numlist)):
    if numlist[i]>avg:
        print("{} ".format(numlist[i]),end='')
