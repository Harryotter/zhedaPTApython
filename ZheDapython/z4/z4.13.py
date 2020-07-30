#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=float(input())
def factorial(num):
    res=1
    if num==0:
        pass
    else:
        for i in range(1,num+1):
            res=res*i
        return res
alist=[1]
blist=[0]
count=1
while (sum(alist)-sum(blist))>=n:
    blist=alist.copy()
    alist.append(1/factorial(count))
    count+=1
print("{:.6f}".format(sum(alist)))
# 首先注意将列表的值赋给另一个列表只是多了一个指向，本身改变另一个也会(同时！！)改变;
# 用列表的copy()方法可以解决赋值的指向问题
# e课近似为级数1+1/1!+1/2!+⋯+1/n!的和，最终要求的是前n+1项的和即i+1项的alist的和



