a,n=map(int,input().split())
numlist=sum([int(str(a)*i) for i in range(1,n+1)])
print("s = {}".format(numlist))