#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2
_author_ = ' Hermione'
import math
a, b, c = map(int, input().split())
s = (a + b + c) / 2
if a + b > c and a + c >b and b + c > a and a > 0 and b > 0 and c > 0:
    m = s * (s - a) * (s - b) * (s - c)
    area = math.sqrt(m)
    perimeter = a + b + c
    print("area = {:.2f}; perimeter = {:.2f}".format(area, perimeter))
else:
    print("These sides do not correspond to a valid triangle")
# 本题要注意避免使用or来连接判断，因为or只要有一个符合后面就不判断了
# 很容易出现 1 2 3,当判断发现a+b=3 不符合 a+b<c or a+c<b or b+c<a的第一个式子a+b<c时
# 就判断不符合该if,转而执行else,导致错误
