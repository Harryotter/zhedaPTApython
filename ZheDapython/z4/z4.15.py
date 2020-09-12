#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
m=int(input())
count=0
for a in range(m//5,0,-1):
    for b in range(m//2,0,-1):
        for c in range(m//1,0,-1):
            if a*5+b*2+c*1==m:
                print("fen5:{}, fen2:{}, fen1:{}, total:{}".format(a,b,c,(a+b+c)))
                count=count+1
print("count = {}".format(count))