#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=list(map(int,input().split()))
for i in range(0,9,3):
    b=a[i:i+3]
    print("{:>4d}{:>4d}{:>4d}{:>4d}{:>4d}".format(b[0],b[1],b[2],max(b),sum(b)))
# 本题很巧妙，借鉴的一个大佬的思路只要找到每行的头，其他元素根据每行的头来确定


