#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=input().strip()
b=input()
c=[]
for i in n:
    if 65<=ord(b.strip())<=90:
        if i==b.strip() or i==chr(ord(b.strip())+32):
            c.append("")
        else:
            c.append(i)
    elif 97<=ord(b.strip())<=122:
        if i==b.strip() or i==chr(ord(b.strip())-32):
            c.append("")
        else:
            c.append(i)
    else:
        if i==(b.strip()):
            c.append("")
        else:
            c.append(i)
print("result: {}".format("".join(c)))


