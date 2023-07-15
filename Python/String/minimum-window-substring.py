
"""
Brute force solution,  
Check all possible window lengths O(s**2), and check if t is in that window. O(t)
while checking we use hashmaps => roughly O(s+t)

O(n*n*m) time complexity, O(n+m) space complexity,
where n = len(s) and m = len(t)
"""
def minWindow(s:str, t:str):
	if not t:return ''
	def inWindow(window, substr):
		w_map, s_map = {}, {}
		for c in window: 
			w_map[c] = w_map.get(c, 0) + 1
		for c in substr: 
			s_map[c] = s_map.get(c, 0) + 1
		for c in s_map:
			if w_map.get(c, -1) < s_map[c]:
				return False
		return True

	res = s
	for start in range(len(s)):
		if start+len(t) > len(s):
			return res
		for end in range(start+len(t), len(s)+1):
			if inWindow(s[start:end], t):
				res = res if len(res) < end-start-1 else s[start:end]


# Linear time and O(len(s)+len(t)) space
def minWindow2(s:int, t:int):
	hashmap, window = {}, {}
	for c in t:
		hashmap[c] = hashmap.get(c, 0) + 1

	res, resLen = [-1, -1], float('inf')
	have, need = 0, len(t)
	l = 0
	for r in range(len(s)):
		char = s[r]
		window[char] = window.get(char, 0) + 1

		if char in hashmap and window[char] <= hashmap[char]:
			have += 1

		while have == need:
			if r-l+1 < resLen:
				resLen = r-l+1
				res = [l, r]
			window[s[l]] -= 1
			if s[l] in hashmap and window[s[l]] < hashmap[s[l]]:
				have -= 1
			l += 1
	l, r = res
	return s[l:r+1] if resLen != float('inf') else ""


# linear time, O(len(t)) space
def minWindow3(s:int, t:int):
	hashmap = {}
	# populate the hashmap with the characters we need, the more negative the number
	# is, then the more instances of the character we want in our window
	for c in t:
		hashmap[c] = hashmap.get(c, 0) - 1

	res, resLen = 0, float('inf')
	start = 0 
	need = len(t)

	# continuously add more characters to our window
	for end in range(len(s)):
		char = s[end]
		# if we just added a desired character
		if char in hashmap:
			# if we don't already have enough of this character in our window, 
			# update the need to show that we have found a desired character
			if hashmap[char] < 0:
				need -= 1
			# if this goes above 1, then we simply have too many in our window
			hashmap[char] += 1

		# if we have all we need in our window already, great! but can we shrink the window?
		while need == 0:
			# if this current window is smaller than the last recorded window length, 
			# update the record
			if end-start+1 < resLen:
				resLen = end-start+1
				res = start
			# now we are about to remove the leftmost element from our window, 
			# so we do some cleaning up if the character is a desired character
			if s[start] in hashmap:
				# if the character is a desired character, then decrement its value in the hashmap.
				# Note that the value could be positive, meaning we have an excess in the 
				# current window. Now we have one less.
				hashmap[s[start]] -= 1
				# if after removing that value, we don't have enough, then we update our need
				if hashmap[s[start]] < 0:
					need += 1
			# at this point we are done processing this character, and are free to remove it.
			# if the character is useful, we would need it now and be forced to extend the 
			# right boundary on subsequent iterations.
			start += 1

	# print(res, resLen)
	return s[res:res+resLen] if resLen != float('inf') else ""



print(minWindow4('ADOBECODEBANC', 'ABC'))
print(minWindow4('BTXUAGYGUIPHYBMER', 'BUY'))