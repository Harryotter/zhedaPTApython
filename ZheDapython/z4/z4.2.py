#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m,n=map(int,input().split())
cnt=0
res=0
def is_primer(num):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                return False
        else:
            return True
    else:
        return False
for i in range(m,n+1):
    if is_primer(i) is True:
        cnt+=1
        res+=i
print("{} {}".format(cnt,res))
# 首先要明确素数定义，注意1 和 2的特殊性



