N=int(input())
numlist=[1/i if i%2==1 else 0 for i in range(1,2*N) if i%2==1 ]
S=sum(numlist)
print("sum = {:.6f}".format(S))
#输入N位数时，奇数列达到1/(2N-1)
#因此range范围到(2N-1)+1  #(同时注意range右取取不到)
