#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
flag=False
for i in range(m,n+1):
    a=[]
    for j in range(1,int(pow(i,0.5))+1):
        if i%j==0:
            if (j not in a ) and (i/j not in a):
                a.append(j)
                a.append(i//j)
    a.remove(i)
    a.sort()
    if sum(a)==i:
        flag=True
        print(str(i)+" = ",end='')
        print(*a,sep=' + ')
if not flag:
    print('None')

# 本题涨知识了！
# 根号几完全可以用某某数的1/2次方来表示
# print(*a)其实是指将a列表中的元素一次打印出来
# 而sep='+'则是表示用+号来连接内容
