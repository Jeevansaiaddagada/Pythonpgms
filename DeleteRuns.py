from pcinput import getString
total=""
temp1=""
temp2=""
temp3=""
count1=True
while True:
    x= getString("enter a string: ")
    y=bool(x)
    if y==True:
        while bool(count1)==True:
            count=0
            count1=0
            for i in x:
                if count==0:
                    temp1=i
                    print("16 temp1 ",temp1)
                if count>=1:
                    temp2=i
                    print("19 temp2 ",temp2)
                if temp1!=temp2 and count>=1:
                    if count1==0:
                        temp3=temp1
                        print("23 temp3 ",temp3)
                        temp1=temp2
                        print("25 temp1 ",temp1)
                        total+=temp3
                        print("27 total ",total)
                    if count1!=0:
                        temp3=temp2
                        print("30 temp3 ",temp3)
                        temp1=temp2
                        print("32 temp1 ",temp1)
                        total+=temp3
                        print("34 total ",total)
                        count1=0
                if temp1==temp2 and count>=1:
                    count1=1
                count+=1
                print("39 count: ",count)
                print("40 total :",total)
                print("41 count1: ",count1)
            x=total
