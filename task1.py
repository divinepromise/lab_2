import math

def square_root(a):
	x=a/2
	epsilon=0.0000001
	while True:
		print(x)
		y=(x+(a/x))/2
		if abs(y-x) < epsilon:
			return y
			break
		x=y


result = square_root(3)

print(result)
