#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
numlist1=[i*i for i in range(m,n+1)]
numlist2=[1/i for i in range(m,n+1)]
s1=sum(numlist1)
s2=sum(numlist2)
print("sum = {:.6f}".format(s1+s2))