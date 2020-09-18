#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
# 先构建一个存放数组的空列表
mlist=[]
# 构建一个存放行最大值的空列表
maxlist=[]
# 构建一个存放列最小值得空列表
minlist=[]
# 循环遍历n阶矩阵的n行(获取行最大值)
for i in range(n):
    mlist.append(list(map(int,input().split())))
    maxlist.append(max(mlist[i]))
# #本处较难理解：(借鉴其他大佬的地方)
# 循环遍历n阶矩阵的n列(获取列最小值)
for j in range(n):
    minlist.append(min([mlist[i][j] for i in range(n)]))
for i in range(n):
    for j in range(n):
        if maxlist[i]==minlist[j] and maxlist[i]==mlist[i][j]:
            print(i,j)
            exit()    # 表示当满足if后，就执行退出
print("NONE")  # 此处不能写在if条件分支下，否则每条不符合if的语句都会打印出none
# 本题最大的收获就是将数组化成求列表的每行每列的最大值最小值





