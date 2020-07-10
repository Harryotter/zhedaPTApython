#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m=int(input())
numlist=list(str(m))
numlist.reverse()
if numlist[0]=='0'and numlist[1]=='0':
    print("{}".format(int(numlist[2])))
elif numlist[0]=='0'and numlist[1]!='0':
    print("{}{}".format(int(numlist[1]),int(numlist[2])))
else:
    print("{}{}{}".format(int(numlist[0]),int(numlist[1]),int(numlist[2])))
# 因为list只能56



