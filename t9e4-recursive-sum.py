#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

def sum(x):
	if len(x) == 1:
		return x[0]
	return x[0] + sum(x[1:])

print(sum([1,2,3,4,5]))