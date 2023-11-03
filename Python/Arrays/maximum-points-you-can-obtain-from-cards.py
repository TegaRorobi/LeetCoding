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


# first of all, select all the cards on the right. (imagining we took cards only from the right)
# next, remove the outermost card on the right from consideration, and then take the outermost one on the left.
# continue removing from the right and taking from the left and keep recording the total as you go. We are done 
# when we now have all cards from the left and no more right cards.
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
# progress to selecting right cards.
def maxScore2(cardPoints: list[int], k:int) -> int:
	l, r = k-1, len(cardPoints)-1
	res = total = sum(cardPoints[:k])
	while l >= 0:
		total += (cardPoints[r] - cardPoints[l])
		res = max(res, total)
		l, r = l-1, r-1
	return res


'''
k=3

1, 2, 3, {4, 5, 6, 1} points=6

1, 2, {3, 4, 5, 6}, 1 points=4

1, {2, 3, 4, 5}, 6, 1 points=8

{1, 2, 3, 4}, 5, 6, 1 points=12
'''

print(maxScore2([1,2,3,4,5,6,1], 3))
print(maxScore2([9,7,7,9,7,7,9], 7))
print(maxScore2([2, 2, 2], 2))
