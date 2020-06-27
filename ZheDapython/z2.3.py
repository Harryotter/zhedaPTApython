while 1:
    a=int(input())
    if a==1:
        print("==========1=========")
        e=int(input())
        if e<=50:
            print("cost = {:.2f}".format(e*0.53))
        elif e>50:
            x=50*0.53+(e-50)*0.58
            print("cost = {:.2f}".format(x))
        elif e<0:
            print("Invalid Value!")
    elif a==2:
        print("=========2========")
        a = int(input())
        if a < 0:
            print("Invalid Value!")
        elif a <= 50:
            cost = a * 0.53
            print("cost = {:.2f}".format(cost))
        else:
            cost = 50 * 0.53 + (a - 50) * 0.58
            print("cost = {:.2f}".format(cost))
    if a==3:
        break

# x=(51-50)*0.58+26.50
# print("cost = {:.2f}".format(x))
