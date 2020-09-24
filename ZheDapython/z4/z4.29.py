#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
a=list(input().split())
b=list(input().split())
re=[]
lista=a[1:]
listb=b[1:]
for i in lista:
    if i not in listb and i not in re:
        re.append(i)
for j in listb:
    if j not in lista and j not in re:
        re.append(j)
print(' '.join(re))
# 本题有个关键提示引导用join()方法，就是最后一个字符后面，第一个字符之前都不能有空格（这点比较坑，用format不太好实现）
# 本题也不需要将每行输入的数字个数单独拿出来，只需要索引的时候切片从索引1开始
