#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
num=input()
numlist=[int(n) for n in num]
print("{} {}".format(len(numlist),sum(numlist)))
# 本题不难，只是建立一个整数列表的思路不同于一般将字符串转换成列表