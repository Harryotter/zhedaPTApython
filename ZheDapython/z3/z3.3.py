#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
inputstr=input()
m,n=input().split()
strlist=[str(n) for n in inputstr]
count_m=0
count_n=0
strlist.reverse()
for i in strlist:
    if n==i:
        print("{} {}".format(len(strlist)-count_n-1,n))
    count_n+=1
for i in strlist:
    if m==i:
        print("{} {}".format(len(strlist)-count_m-1,m))
    count_m+=1
# 本题不适合用index来获取索引位置，因为当重复字符时候，总是打印第一个
# 目前没有想到利用index的解决办法

