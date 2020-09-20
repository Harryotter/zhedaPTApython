#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
sum1=1
sum2=0
for i in range(1,n+1,2):
    for j in range(i,0,-1):
        sum1*=j
    sum2+=sum1
    sum1=1
print("n={},s={}".format(n,sum2))
# 本题主要是累积和累和的思想，并且注意每小部分累积了之后进行下一部分的阶乘时，要注意清一
