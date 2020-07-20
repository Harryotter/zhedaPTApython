# coding=utf-8
# Version: python3.6.0
# Tools: Pycharm 2017.3.2
_author_ = ' Hermione'
str1 = input()
s = '1234567890abcdefABCDEF'
c = ""
for item in str1:
    if item in s:
        c = c + item
if c == '':
    print('0')
elif str1.find(c[0]) > str1.find('-'):
    print(-int(c, 16))
else:
    print(int(c, 16))



# 本题首先要分清十六进制字符是：逢16进一的字符
