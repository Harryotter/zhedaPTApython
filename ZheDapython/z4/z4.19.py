#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
a=[]
sum=0
for i in range(n):
    s=input()
    a.append([int(b) for b in s.split()])
for j in range(n):
    for k in range(n):
        if j!=n-1 and k!=n-1 and j+k!=n-1:
            sum+=a[j][k]
print(sum)
# 本题的重要知识点：用列表建立一个矩阵(即二维数组)
# 注意：思维不要定势，Python中的列表可以表示数组




