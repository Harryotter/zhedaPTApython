#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
num=input().split()
numlist=[int(n) for n in num]
numlist=numlist[1:]
countlist=[]
count=1
for i in range(len(numlist)):
    for k in range(i+1,len(numlist)):
        if numlist[i]==numlist[k]:
            count+=1
    countlist.append(count)
    count=1
a=countlist.index(max(countlist))
print("{} {}".format(numlist[a],max(countlist)))
# 本题难度不大，就是要注意省题：第一行输入的第一个整数是输入整数的个数
# 计算的时候要把第一个数让掉


