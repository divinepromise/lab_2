import math

def estimate_pi():
	k=0
	summation=0
	mul = 2*math.sqrt(2) / 9801
	while True:
		numerator = math.factorial(4*k) * (1103 + 26390*k)
		denominator = (math.factorial(k))**4 * 396**(4*k)
		result =  mul * numerator/denominator
		summation += result

		if abs(result) < 1e-15:
			break
		k+=1

	final_result = 1/summation
	return final_result

estimated_pi = estimate_pi()
print("estimated pi= ",estimated_pi,"main pi= ",math.pi)
