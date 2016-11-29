#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
#

def mul(a, b):
	if b == 1:
		return a
	return a + mul(a, b-1)

a = int(input("a? "))
b = int(input("b? "))

print(mul(a, b))