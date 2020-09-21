#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=list(map(int,input().split()))
for i in range(3):
    print("{:4d}{:4d}{:4d}".format(a[i],a[i+3],a[i+6]))