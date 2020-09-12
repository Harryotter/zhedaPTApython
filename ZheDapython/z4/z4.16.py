#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
x,y,z=map(int,input().split())
if x+y<=z or x+z<=y or y+z<=x:
    print("no")
else:
    print("yes")
