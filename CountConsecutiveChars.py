from pcinput import getString
while True:
    x= getString("enter a string: ")
    y=bool(x)
    if y==True:
        count=1
        run=1
        run1=1
        temp=""
        temp1=""
        for i in x:
            if temp==i:
                if temp1!= i and count!=1:
                    count+=1
                count+=1
                run+=1
                if run>run1:
                    run1=run
                temp1=i
            else:
                run=1
            temp=i
        if count>1:
            print("{} {}{}{} {}".format("count",count,"\n","max",run1))
        else:
            print("{} {}{}{} {}".format("count","0","\n","max","0"))
    else:
        print("{} {}{}{} {}".format("count","0","\n","max","0"))
        break
