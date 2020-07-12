#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
ch=input()
strch=input()
strlist=[str(n) for n in strch]
strlist.reverse()
if ch not in strlist:
    print("Not Found")
else:
    print("index = {}".format(len(strlist)-strlist.index(ch)-1))

# 待修正部分正确的方法二：
# ch=input()
# strch=input()
# strlist=[str(n) for n in strch]
# strlist.reverse()
# for i in strlist:
#     if ch==i:
#         print("index = {}".format(len(strlist)-strlist.index(ch)-1))
#         break
#     else:
#         print("Not Found")
#         break
