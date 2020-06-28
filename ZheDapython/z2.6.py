#coding=utf-8
#Version: python3.6.0
#Tools: Pycharm 2017.3.2
#_author_ = ' Hermione'
N=int(input())
numlist=[i/(2*i-1) if i%2==1 else -i/(2*i-1) for i in range(1,N+1)]
S=sum(numlist)
print("{:.3f}".format(S))
#本题与z2.5比较，range序列个数容易搞错
#本题分子间隔为一，因此右端应为输入个数加一
