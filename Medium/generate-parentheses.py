class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        from itertools import permutations
        combs = permutations('()'*n, 2*n)
        output = []
        for comb in combs:
            strcomb = ''.join(comb)
            if strcomb.startswith('('):
                if strcomb.endswith(')'):
                    if strcomb not in output:
                        output.append(strcomb)
        return output

sol = Solution()
print(sol.generateParenthesis(3))