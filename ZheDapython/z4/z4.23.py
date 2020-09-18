#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
a=[]
count=0
for i in range(m):
    s=input()
    a.append([int(b) for b in s.split()])
for i in range(1,m-1):
    for j in range(1,n-1):
        if a[i][j]>a[i+1][j] and a[i][j]>a[i][j+1] and a[i][j]>a[i-1][j] and a[i][j]>a[i][j-1]:
            print("{} {} {}".format(a[i][j],i+1,j+1))
            count+=1
if count==0:
    print("{} {} {}".format("None",m,n))