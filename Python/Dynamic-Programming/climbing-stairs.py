
def climbStairs(n:int) -> int:
	one, two = 1, 1
	# we don't use i, so it is equivalent to range(n-1), but this better helps
	# to visualize the dynamic programming problem.
	# [ 0 , 1 , 2 , 3 , 4 , 5]
	#
	#   ^   ^   ^   ^   ^   ^
	#  5+3 3+2 2+1 1+1  1   1
	#  =8  =5  =3   =2

	# fun fact: these are just the numbers of the fibonacci sequence!
	
	for i in range(n-2, -1, -1):
		one, two = one+two, one
	return one

print(climbStairs(5))