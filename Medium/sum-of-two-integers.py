
def getSum(a:int, b:int) -> int:
	mask = (1<<32)-1
	while b&mask:
		carry = (a&b) << 1 # all this gets is the carry value and shifts it to the left
		a = a ^ b  # this adds them, but doesn't account for the carry 1
		b = carry

	return a & mask if b > 0 else a

print(getSum(-11, -9))

# 0b11111111111111111111111111110110