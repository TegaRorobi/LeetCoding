
def longestCommonPrefix1(strs: list[str]) -> str:
	lcp = strs[0]
	for string in strs[1:]:
		common = ""
		for i in range(len(lcp) if len(lcp) < len(string) else len(string)):
			if lcp[i] == string[i]:
				common += lcp[i]
			else:
				break
		lcp = common
	return lcp

def longestCommonPrefix(strs: list[str]) -> str:
	lcp = ""
	for i in range(len(strs[0])):
		chr = strs[0][i]
		for s in strs:
			if i<len(s) and s[i] != chr:
				return lcp 
		lcp += chr
	return lcp 


print(longestCommonPrefix(strs = ["flower","flow","flight"]))
print(longestCommonPrefix(strs = ['ab', 'a']))
print(longestCommonPrefix(strs = ['car', 'cir']))
