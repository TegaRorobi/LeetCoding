
def groupAnagrams(strs: list[str]) -> list[list[str]]:
	res = []
	def isAnagram(s1, s2):
		hashmap = {}
		for c in s1: hashmap[c] = hashmap.get(c, 0) + 1
		for c in s2: hashmap[c] = hashmap.get(c, 0) - 1
		for val in hashmap.values():
			if val != 0: 
				return False
		return True

	for string in strs:
		is_part_of_group = False
		for group in res:
			if len(group[0]) == len(string) and isAnagram(group[0], string):
				group.append(string)
				is_part_of_group = True 
				break
		if not is_part_of_group:
			res.append([string])
	return res 


def groupAnagrams2(strs: list[str]) -> list[list[str]]:
	res, hashmap = [], {}
	for s in strs:
		s2 = ''.join(sorted(s))
		if s2 in hashmap:
			res[hashmap[s2]].append(s)
		else:
			res.append([s])
			hashmap[s2] = len(res) - 1
	return res




print(groupAnagrams2(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams2([""]))
print(groupAnagrams2(["a"]))