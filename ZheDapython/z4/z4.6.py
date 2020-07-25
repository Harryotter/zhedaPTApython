#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
def fib(num):
    a,b=0,1
    for j in range(num+1):
        a,b=b,a+b
    return a
if n<1:
    print("Invalid.")
else:
    for i in range(n):
        print("{:11d}".format(fib(i)),end='')
        if (i+1)%5==0:
            print("\n",end='')
# 注意两个值同时赋值的写法
# 整数部分11位的写法：11d