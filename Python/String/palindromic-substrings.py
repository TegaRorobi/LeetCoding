
def countSubstrings(s: str) -> int:
	if not s: return 0
	count = 0 
	def extendPalindrome(l, r):
		nonlocal count
		while l>=0 and r < len(s) and s[l] == s[r]:
			count += 1; l-= 1; r += 1
	for i in range(len(s)):
		extendPalindrome(i, i)
		extendPalindrome(i, i+1)
	return count


print(countSubstrings('aaa'))
print(countSubstrings('abc'))