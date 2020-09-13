#coding=utf-8 
#Version: python3.6.0 
#Tools: Pycharm 2017.3.2 
_author_ = ' Hermione'
n=int(input())
for i in range(pow(10,n-1),pow(10,n)):
    j=i
    sum=0
    while j>=1:
        sum=sum+pow(j%10,n)
        j=j//10
    if sum==i:
        print(i)

# 本题要分清“//”和“%”，//可以得到几位数除最后一位的位数，%可以得到最后一位的数字
# 另外要注意第八行sum=0必须放在for循环内，不能放在for循环外面(乳沟放在for循环的外面，sum的值将一直累加)