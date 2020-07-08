#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
x,y,z=map(int,input().split())
numlist=[]
numlist.append(x)
numlist.append(y)
numlist.append(z)
numlist2=sorted(numlist)
print("{}->{}->{}".format(numlist2[0],numlist2[1],numlist2[2]))
#灵活运用python中自带的排序函数
#列表的append方法只能一个一个添加
