#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=input()
count=0
c=[]
for i in n:
    if 65<=ord(i)<=90 and i not in c:
        c.append(i)
        count+=1
if count==0:
    print("Not Found")
else:
    print("".join(c))