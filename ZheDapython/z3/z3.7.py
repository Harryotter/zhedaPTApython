#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
# num=input()
# numlist=list(map(int,input().split()))
# num_max=max(numlist)
# num_index=numlist.index(num_max)
# print("{} {}".format(num_max,num_index))
# 注意列表的输入写法，之前的for n in list 的写法有出现对象不能迭代的情况，目前没找到解决方法
# 法二：解决了之前对象迭代错误问题，可能是软件问题，重新输入一遍即可
b=input()
a=input().split()
alist=[int(n) for n in a]
num_max=max(alist)
num_index=alist.index(num_max)
print("{} {}".format(num_max,num_index))