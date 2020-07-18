# coding=utf-8
# Version: python3.6.0
# Tools: Pycharm 2017.3.2
_author_ = ' Hermione'
n = input().strip()
count = 0
c = []
for i in n:
    if 65 <= ord(i) <= 90 and i not in c:
        if chr(ord(i) + 32) not in c:
            c.append(i)
            count += 1
    elif 97 <= ord(i) <= 122 and i not in c:
        if chr(ord(i) - 32) not in c:
            c.append(i)
            count += 1
    if count == 10:
        break
if count < 10:
    print("not found")
else:
    print("".join(c))
# 本题容易搞错的地方就是当英文字母的长度小于10就输出"not found"而不是输入的长度
# 大小写字母不分也需要分类讨论


