#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
lower,upper=map(int,input().split())
if lower<=0 or lower>upper or upper<=0 or upper>100 or lower>100:
    print("Invalid.")
else:
    print("fahr celsius")
    for i in range(lower,upper+1,2):
        print("{}{:>6.1f}".format(i,5*(i-32)/9))
#搞了大半天，报错原来是因为后面有个"Invalid."中有个点，太坑了