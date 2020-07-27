#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
c=[]
def fib(num):
    a,b=2,3
    for j in range(1,num):
        a,b=b,a+b
    return a
for i in range(1,n+1):
    if i<=1:
        c.append(fib(i)/1)
    else:
        c.append(fib(i)/fib(i-1))
print("{:.2f}".format(sum(c)))
# 本题具有迷惑性，只要将序列分子分母拎出来找规律
# 另外求斐波那契数的函数的起始值需要注意，最后返回一个值
