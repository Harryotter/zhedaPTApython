#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
A,B=map(int,input().split())
numlist=range(A,B+1)
X=sum(numlist)
for k in range(B+1-A):
    print("{:>5d}".format(numlist[k]),end='')
    if (k+1)%5==0 :
        print("\n",end='')
    elif k==B-A:
        print("\n",end='')
print("Sum = {:d}".format(X))
# 第11、13行中： print("\n",end='') 其中end=''是为了让打印的二维列表与最后的sum和之间不要空一行
# 即是紧接着换行打印
# print("{:>5d}".format(numlist[k]),end='')中"{:>5d}"，不能有空格："{:>5d} "！！！





