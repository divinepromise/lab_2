import math

def square_root(a):
	x=a/2
	epsilon=0.0000001
	while True:
		y=(x+(a/x))/2
		if abs(y-x) < epsilon:
			return y
			break
		x=y

def test_square_root(a):

	for value in a:
		result_1 = square_root(value)
		result_2 = math.sqrt(value)
		spaces="    "
		print(value,spaces,result_1,spaces,result_2,spaces,abs(result_1-result_2))

test_square_root(range(1,10))


