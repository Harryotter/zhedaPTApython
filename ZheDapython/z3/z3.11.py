#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=input().split()
b=list(a)
b.sort()
print("After sorted:\n{}\n{}\n{}\n{}\n{}".format(b[0],b[1],b[2],b[3],b[4]))
# 即使是非整数，也能用列表的sort()方法，只不过按照unicode码的大小排序
# sort()方法按照从小到大来实现