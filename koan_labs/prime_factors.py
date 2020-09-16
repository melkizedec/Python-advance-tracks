def largest_prime_factor(args):
	# TODO: Your code goes here
	rng = range(1, args)
	lst = []
	for x in rng:
		if args % x == 0:
			lst.append(x)

	return max(lst)
	