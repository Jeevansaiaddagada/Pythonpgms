import math
amount=float(input('amount in dollars and cents :'))
print(amount)
i=amount//100
j=amount%100
newamount=j
#newamount=amount-(i*100)
print(int(i),  '100 Dollar Bills')
i=newamount//50
j=newamount%50
newamount=j
print(int(i), '50 Dollar Bills')
i=newamount//20
j=newamount%20
newamount=j
print(int(i), '20 Dollar Bills')
i=newamount//10
j=newamount%10
newamount=j
print(int(i), '10 Dollar Bills')
i=newamount//5
j=newamount%5
newamount=j
print(int(i), '5 Dollar Bills')
i=newamount//1
j=newamount%1
newamount=j*100
#print(newamount)
print(int(i), '1 Dollar Bills')
#i=newamount//.25
#j=newamount%.25
i=newamount//25
j=newamount%25
newamount=j
print(int(i), '25 Cent coins')
#i=newamount//.10
#j=newamount%.10
i=newamount//10
j=newamount%10
newamount=j
print(int(i), '10 Cent coins')
#i=newamount//.05
#j=newamount%.05
i=newamount//5
j=newamount%5
newamount=j
print(int(i), '5 Cent coins')
#i=int((newamount)//.01)
#j=((newamount)%.01)
i=newamount//1
#print("i=", i)
j=round((newamount%1),2)
newamount=j
z=i+j
print(int(z), '1 cent coins')
#print(newamount)
#print(j)
#print(int(math.ceil(i+newamount)), '1 Cent coins')