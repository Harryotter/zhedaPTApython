#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
rep=min(m,n)
mult=m*n
a=[]
for i in range(rep,0,-1):
    if m%i==0 and n%i==0:
        a.append(i)
        break
print("{} {}".format(a[0],mult//a[0]))
# 本题须知一条性质：两数之积除以最大公约数即得最小公倍数，两者求一个即可
# 直接除以的话会有小数，用"//"来只取商部分

