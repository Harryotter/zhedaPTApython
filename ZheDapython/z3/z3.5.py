#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
strlist=input()
strlist=[str(n) for n in strlist]
numlist=list("0123456789")
strlist2=[]
for i in range(len(strlist)):
    if  strlist[i] in numlist:
        strlist2.append(strlist[i])
for j in range(len(strlist2)):
    if len(strlist2)>1 and strlist2[0]=='0' :
       strlist2.remove(strlist2[0])
    elif len(strlist2)==1:
       strlist2[0]=0
for k in range(len(strlist2)):
    print(int(strlist2[k]),end="")
# 本题不难，但是两个测试点都考验了对于整数的理解
# 整数首位非零
# 但若只有一个零，也是不能删除的
