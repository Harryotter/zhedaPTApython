#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=input()
b=list(a)
for i in range(len(b)):
    if b[i]=='#':
        b[i]=""
        break
    elif 65<=ord(b[i])<=90:
        b[i]=chr(ord(b[i])+32)
    elif 97<=ord(b[i])<=122:
        b[i]=chr(ord(b[i])-32)
c=''.join(b)
c.strip()
print(c)
# 本题不难，就是ord()、chr()要分清楚
# ord(字符型)：把字符转换成ASCII码，中文则是Unicode码
# chr(整型)：把整型值转换成相应的字符