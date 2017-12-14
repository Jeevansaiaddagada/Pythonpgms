from pcinput import getFloat
from pcinput import getInteger
x=getFloat("enter today's tuition: ")
y=getFloat("enter rate of increase: ")
yr=getInteger("enter number of years: ")
temp1=x
i=0
j=0
total=0
print("year tuition")
while i<yr:
    x*=(1+(.01*y))
    i+=1
    print("{:>4d} {:>10,.2f}".format(i,x))
temp2=x
while j<=3:
    total+=x
    x*=(1+(.01*y))
    j+=1

print('\n'"Given today's tuition: {:,.2f}, at a rate of {:.2f}%, tuition in {} years is {:,.2f}. The four-year tuition in {} years is {:,.2f}".format(temp1,y,yr,temp2,yr,total))
