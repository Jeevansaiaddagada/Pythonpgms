from pcinput import getFloat
from pcinput import getString
while True:
	units = getString("Enter units: ")
	dis = getFloat("Enter a distance: ")
	if units == 'mi':
		#print("1")
		kilo = dis*1.609
		print("distance in miles: {:.2f}".format(dis))
		print("distance in km is: {:.2f}".format(kilo))
		break
	elif units == "km":
		#print("2")
		miles = dis /1.609
		print("distance in km: {:.2f}".format(dis))
		print("distance in mi is: {:.2f}".format(miles))
		break

	else:
		#print("3")
		print("wrong input!")
		break

	