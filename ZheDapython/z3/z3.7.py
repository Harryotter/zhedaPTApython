#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
num=input()
numlist=list(map(int,input().split()))
num_max=max(numlist)
num_index=numlist.index(num_max)
print("{} {}".format(num_max,num_index))
# 注意列表的输入写法，之前的for n in list 的写法有出现对象不能迭代的情况，目前没找到解决方法