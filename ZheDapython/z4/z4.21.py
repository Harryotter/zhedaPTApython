#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m=int(input())
re = []
for i in range(m):
    n=int(input())
    count=0
    a=[]
    for h in range(n):
        s=input()
        a.append([int(b) for b in s.split()])
    for j in range(n):
        for k in range(n):
            if j>k:
                if a[j][k]==0:
                    count+=1
    if count==n*(n-1)/2:
        re.append(0)
    else:
        re.append(1)
for i in range(m):
    if re[i]==0:
        print("YES")
    else:
        print("NO")
# 本题我卡在了如何收集好所有下三角区的值结束循环和怎么判断全为0

