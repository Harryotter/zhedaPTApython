#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
def judge(inputlist,qlist,judgelist):
    lastnum=inputlist[-1]
    inputlist = inputlist[:17]
    m=0
    qsum=0
    for i in inputlist:
        if '0' <= i <= '9':
            qsum+=int(i)*qlist[m]
            m+=1
        else :
            return False
    z = qsum % 11
    if lastnum == judgelist[z]:
        return True
    else:
        return False
N=int(input())
count=0
qlist=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
judgelist=list("10X98765432")
# judgelist=['1','0','X','9','8','7','6','5','4','3','2']
for i in range(N):
    inputlist=input()
    if not judge(inputlist, qlist, judgelist):
       print(inputlist)
    else :
       count=count+1
if count==N:
    print("All passed")

# qsum+=int(i)*qlist[m] 这里是加权的和，因此是需要连加的
# list与字符串的转换可以提高写代码速度





