
import  calendar
M,BE= {int(e) for e in input().split()}


if 1 <= M and M <=12:
    if M == 2  :
        if (BE-543)/4 == 501 :
            print("29")
        else:
            print("28")
    else:
        if M == 4 or M == 6 or  M == 9 or M == 11 :
            print("30")
        else:
            print("31")



