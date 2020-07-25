#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
if n==0:
    print("average = {}\ncount = {}".format(0.0,0))
else:
    m=map(int,input().split())
    mlist=list(m)
    res=sum(mlist)
    ave=int(res)/n
    count=0
    for i in mlist:
        if i >=60:
            count+=1
    print("average = {:.1f}\ncount = {}".format(ave,count))
# 本题比较坑的一个点就是肺腑整数也包括0这个情况
# 另外用列表的sum()函数时,列表的类型必须是整型
