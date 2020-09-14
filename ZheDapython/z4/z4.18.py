#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
lista=[]
for i in range(1,n+1):
    lista.append(i)
if n==1:
    print("1")
else:
    while len(lista)>=3:
        lista.pop(2)# 将索引为2的元素出栈
        lista.append(lista.pop(0))# 将出栈的元素的前面的元素放到队列的后面
        lista.append(lista.pop(0))# 原本第一个的元素出栈了，因此此时还是将头元素放到队列的末尾
    print(lista[1])
# 本题是著名的约瑟夫环的问题，这题借鉴了一个大佬的思路：将约瑟夫环线性化
# 将出栈的元素加到队列末尾包含两个动作：先将元素出栈，再将元素加到队列末尾


