def isPalindrome(s):
	# here i am creating a custom function to check if a character is alphanumeric.
	def isAlphaNumeric(char):
		return ( 
			ord(char) in range(ord('a'), ord('z')) or
			ord(char) in range(ord('A'), ord('Z')) or
			ord(char) in range(ord('0'), ord('9'))
		)

	# we could also use the below function but it would need importing a build in library.

	# import string 
	# def isAlphaNumeric(char):
	# 	return char in string.ascii_letters+string.digits

	l, r = 0, len(s)-1

	# we will use two pointers to traverse the string
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