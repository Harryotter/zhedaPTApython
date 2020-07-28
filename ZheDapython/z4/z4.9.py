#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
print("[1] apple\n[2] pear\n[3] orange\n[4] grape\n[0] exit")
count=0
n=input().split()
c=list(n)
for i in range(5):
    count+=1
    if c[i]=="1":
        print("price = 3.00")
    elif c[i]=="2":
        print("price = 2.50")
    elif c[i]=="3":
        print("price = 4.10")
    elif c[i]=="4":
        print("price = 10.20")
    elif c[i]=="0":
        exit()
    else:
        print("price = 0.00")
    if count>5:
        exit()
# 本题要注意的是测试样例是一次性输入的，编写的时候，用for比while更容易判断

