
def hammingWeight(n:int) -> int:
	res = 0 
	while n:
		n = n & (n-1)
		res += 1 
	return res

print(hammingWeight(15))