#medium

#Time complexity: O(n) 
#Space complexity: O(numRows)

# Simply iterate over the string and put the elements into groups of 
# rows, using a j pointer to know the row and a direction variable 
# to know what direction to go to find the next row.
# the direction changes at the ends i.e 0 and the last row(numRows-1)
def convert(s:str, numRows:int) -> str:
	if numRows==1:
		return s
	ans = ['' for _ in range(numRows)]
	j = 0
	direction = -1
	for i in range(len(s)):
		if j == 0 or j == numRows-1:
			direction *= -1
		ans[j] += s[i]
		j += direction
	return ''.join(ans)


# PAYPALISHIRING
""" 3 rows
P     A     H     N
A  P  L  S  I  I  G
Y     I     R
"""

""" 4 rows
P       I      N
A     L S    I G
Y  A    H  R
P       I
"""

print(convert('PAYPALISHIRING', 4))
