#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=input().split()
b=(str(a)).strip()
alist=list(b)
count=0
strc="A,E,I,O,U"
strb="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
for i in strc:
    strb=strb.replace(i,"")
blist=list(strb.strip())
for i in range(len(alist)):
    if alist[i] in blist:
        count+=1
print(count)
# 本题主要注意字符串相减用到replace
# 只有字符串才会有repalce()、strip()
# 将字符串转换成列表形式用list(字符串)
