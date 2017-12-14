from pcinput import getInteger
num = getInteger("enter size of base: ")
while True:
	#num = getInteger("enter size of base: ")
	
	if num == 0:
		break
	if num > 0 and num < 22:
		for g in range (0,num,1):
			print( (g+1) * '*')
		break
	if num < 0 or num >21:
		num = getInteger("try again, enter size of base: ")
		#print("try again")
		continue	
