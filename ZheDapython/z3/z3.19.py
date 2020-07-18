#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
c=[]
b=[]
for i in range(n):
    i=input()
    c.append(len(i))
    b.append(i)
a=c.index(max(c))
print("The longest is: {}".format(b[a]))
# 本题不难，主要注意range()的参数是int型