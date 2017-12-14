from pcinput import getInteger
while True:
    x= getInteger("Enter any integer: ")
    temp= x%13==0 or x%17==0 or x%19==0
    if(x==0):
        print("done!")
        break
    elif ( (x>=13) and (temp ) ):
        print(x,"is divisible by 13, 17 or 19")
    elif (temp==False ):
        print(x,"is NOT divisible 13, 17 or 19")
    else:
        print(x,"is NOT divisible 13, 17 or 19")
