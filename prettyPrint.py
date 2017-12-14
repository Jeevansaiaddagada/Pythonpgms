#x = "apple", 3, 1.4, ("a1", "a2"), ("a1",("b1","b2",("c1","c2","c3"),"b3"),"a2")
#x = [("apple", 3, 1.4, ("a1", "a2"), ("a1",("b1","b2",("c1","c2","c3"),"b3"),"a2"))
#x =["apple", 3, 1.4, ["a1", "a2"], ["a1",["b1","b2",["c1","c2","c3"],"b3"],"a2"]]

def prettyPrint(x):
    def p1(x,c):
        for i in x[0:len(x)]:
            if (type(i) is tuple or (type(i) is list)):
                
                #print("140:" ,type(i))
                p1(i,c+1)
                #print("142: i ",i,"c:",c)
            else:
                print("{}{}".format(("   "*c),(i)))
                
                #print("146:",i, "c:",c)


    p1(x,0)

    


prettyPrint(x)