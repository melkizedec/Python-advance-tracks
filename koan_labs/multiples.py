def multiple_sum():
	#TODO: Your code goes here
	list_number = []
	indie = range(1,1000)
	for x in indie:
		if x % 3 == 0 or x % 5 == 0:
			list_number.append(x)


	return sum(x for x in list_number)
	