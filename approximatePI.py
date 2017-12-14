while True:
	apr = int(input("enter n: "))
	if apr == 0:
		break
	total = 0
	x1 = 1
	i = 1
	def aprox(x1):
		return(4*(1/x1))
	while i <= apr:
		t1 = total
		if i%2 == 0:
			total = total - aprox(x1)
		else :
			total = total + aprox(x1)
		x1 += 2
		i +=1
	print(total)