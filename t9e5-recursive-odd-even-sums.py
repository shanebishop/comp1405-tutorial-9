#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

def sums(x):
	return [sum_even(x), sum_odd(x), zero_count(x)]

def sum_even(x):
	if x[0] % 2 == 0:
		if len(x) == 1:
			return x[0]
		else:
			return x[0] + sum_even(x[1:])
	else:
		if len(x) == 1:
			return 0
		else:
			return 0 + sum_even(x[1:])

def sum_odd(x):
	if x[0] % 2 != 0:
		if len(x) == 1:
			return x[0]
		return x[0] + sum_odd(x[1:])
	if len(x) == 1:
		return 0
	return 0 + sum_odd(x[1:])

def zero_count(x):
	if x[0] == 0:
		if len(x) == 1:
			return 1
		return 1 + zero_count(x[1:])
	if len(x) == 1:
		return 0
	return 0 + zero_count(x[1:])

print(sums([0,1,2,0,3,4,5,0]))