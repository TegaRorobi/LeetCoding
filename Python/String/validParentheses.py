
# Time Complexity: O(n)
# Space Complexity: O(n)

def isValid(s):
	hashmap = {'(':')', '[':']', '{':'}'}
	stack = []
	for char in s:
		if char in hashmap:
			stack.append(char)
		# leaving char!=hashmap[stack.pop()] will throw an exception if the 
		# string starts with a closing parenthesis or had all matched parentheses
		# before, leaving the stack empty and then a closing parenthesis.
		elif not stack or char != hashmap[stack.pop()]:
			return False
	return True if not stack else False

print(isValid('()[]{[]}'))
print(isValid('()[]}'))