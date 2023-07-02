class Solution:
    max_score = 0
    # Brute force, O(k^2) runtime complexity, constant space
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        def brute(l, r, n_cards, score):
            if n_cards == k:
                self.max_score = max(score, self.max_score)
                return
            if l+1 < len(cardPoints):
                brute(l+1, r, n_cards+1, score+cardPoints[l])
            if r-1 > -1:
                brute(l, r-1, n_cards+1, score+cardPoints[r])
        brute(0, len(cardPoints)-1, 0, 0)
        return self.max_score
# a = Solution()
# print(a.maxScore([1,2,3,4,5,6,1], 3))


# first of all select all cards from the left and then gradually remove the innermost 
# card on the left and select one more on the right, this way we get all possible ways
# we can select k cards.
def maxScore(cardPoints: list[int], k:int) -> int:
	l, r = 0, len(cardPoints)-k
	res = outside = sum(cardPoints[r:])
	while r<len(cardPoints):
		outside = cardPoints[l] + outside  - cardPoints[r]
		res = max(res, outside)
		l += 1
		r += 1

	return res


# the difference is that we just select all cards from the left first and then we 
# progress to the right.
def maxScore2(cardPoints: list[int], k:int) -> int:
	l, r = k-1, len(cardPoints)-1
	res = total = sum(cardPoints[:k])
	while l >= 0:
		total += (cardPoints[r] - cardPoints[l])
		res = max(res, total)
		l, r = l-1, r-1
	return res


print(maxScore2([1,2,3,4,5,6,1], 3))
print(maxScore2([9,7,7,9,7,7,9], 7))
print(maxScore2([2, 2, 2], 2))
