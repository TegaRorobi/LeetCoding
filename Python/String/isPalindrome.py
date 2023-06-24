##########################################################

# Time Complexity => O(n)
# Space Complexity => O(1)
def isPalindrome(s):
	def isAlphaNumeric(char):
		return ( 
			ord('a') <= ord(char)  <= ord('z') or
			ord('A') <= ord(char)  <= ord('Z') or
			ord('0') <= ord(char)  <= ord('9')
		)

	l, r = 0, len(s)-1

	# we will use the two pointers to traverse the string
	while l <= r:

		while not isAlphaNumeric(s[l]):
			l+=1
		while not isAlphaNumeric(s[r]):
			r-=1
		if s[l].lower() == s[r].lower():
			l+=1
			r-=1
		else:
			return False
	return True

s = 'A man, a plan, a canal; Panama...'
print(isPalindrome(s))

############################################################################


# Time Complexity => O(n)
# Space Complexity => O(n)
def  isPalindrome(s):
	new_str = ''
	for c in s:
		if c.isalnum():
			new_str += c.lower()
	return new_str == new_str[::-1]


s = 'A man, a plan, a canal; Panama...'
print(isPalindrome(s))