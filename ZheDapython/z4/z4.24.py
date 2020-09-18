#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("{}*{}={:<4d}".format(j,i,i*j),end="")
    print("")
# 易知九九乘法口诀表的规律：第一行一个；第二行两个；第三行个，，，因此列的循环是在行的循环的基础上的
# 不适合走先填满后挖空的思路，因为每一个的数字都是在变化的
# :<4d 是指右边占四位整数
# 本题要注意一个小细节，被乘数为列号


