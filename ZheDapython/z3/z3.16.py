#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=input()
alist=list(a)
blist=[]
for i in range(len(alist)):
    if alist[i] not in blist:
        blist.append(alist[i])
c=''.join(blist)
c.strip()
clist=list(c)
clist.sort()
print(''.join(clist))
# 本题要注意clist.sort()不返回一个新的列表，所以打印出来的值才是空的