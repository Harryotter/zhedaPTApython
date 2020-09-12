#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
count=0
alp=0
dig=0
blank=0
oth=0
s=[]
while True:
    a=list(input())
    count+=1
    s.extend(a)
    if len(s)+count>10:
        count-=1
        break
for i in s:
    if i.isalpha():
        alp+=1
    elif i.isdigit():
        dig+=1
    elif i.isspace():
        blank+=1
    else:
        oth+=1
print("letter = {}, blank = {}, digit = {}, other = {}".format(alp,blank,dig,oth))
# 本题重点在于回车的数量如何计算，count的数量就是回车的数量