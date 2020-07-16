#Version: python3.6.0
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=input()
alist=list(str(a))
b=[]
for i in range(len(list(a))):
    if 65<=ord(alist[i])<=90:
        b.append(chr(155-ord(alist[i])))
    else:
        b.append(alist[i])
c=''.join(b)
print(str(c))
# 这里不能使用暴力解法，因为会将列表中的引号去掉，而若输入有引号就无法输出正确

