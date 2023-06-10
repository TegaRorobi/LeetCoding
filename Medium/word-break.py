
# doesn't solve the problem completely and fails at some edge cases.
def wordBreakCookieCutter(s:str, wordDict:list[str]) -> bool:
	for word in wordDict:
		while s.find(word) >= 0:
			loc = s.find(word)
			s = s[:loc]+s[loc+len(word):]
	return not bool(s)



def wordBreak(s:str, wordDict:list[str]) -> bool:
	dp = [False] * (len(s)+1)
	dp[len(s)] = True

	for i in range(len(s)-1, -1, -1):
		for w in wordDict:
			if len(s[i:]) >= len(w) and s[i:i+len(w)] == w:
				dp[i] = dp[i+len(w)]
	return dp[0]

print(wordBreakCookieCutter('carsrs', ['ca', 'rs']))
