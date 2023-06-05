
def wordBreak(s:str, wordDict:list[str]) -> bool:
	for word in wordDict:
		while s.find(word) >= 0:
			loc = s.find(word)
			s = s[:loc]+s[loc+len(word):]
	return not bool(s)

print(wordBreak('neetcodeneetleetcodeleetneetj', ['neet', 'leet', 'code']))
