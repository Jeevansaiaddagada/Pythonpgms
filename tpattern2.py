from pcinput import getInteger
num = getInteger("enter integer number: ")
while True:
	#num = getInteger("enter integer number: ")
	
	if num == 0:
		break
	if num > 0 and num < 22:
		for g in range (num-1,-1,-1):
			#print(g)
			print(g * ' ' + (num-g) * '*')
		break
	if num < 0 or num >21:
		num = getInteger("try again, enter integer number: ")
		continue	
