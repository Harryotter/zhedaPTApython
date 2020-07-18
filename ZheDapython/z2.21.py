#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n = input()
count=0
print(n)
for i in range(len(n)):
    if n[i] == n[len(n) -1- i]:
       count+=1
if count==len(n):
    print("Yes")
else:
    print("No")
# 本题也可用逆序序列来验证回文序列
# 本题注意题意，在输出yes、no之前要输出一次输入的字符串
