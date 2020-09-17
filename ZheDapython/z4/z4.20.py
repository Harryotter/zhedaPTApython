#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
sum=0
a=[]
for i in range(m):
    s=input()
    a.append([int(b) for b in s.split() ])
for j in range(m):
    for k in range(n):
        sum+=a[j][k]
        if k==n-1:
            print(sum)
            sum=0
# 本题还是要掌握python中的数组的表示