class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def isValid(string):
            left_count = 0
            for char in string:
                if char == '(':
                    left_count += 1
                elif char == ')':
                    left_count -= 1 
                if left_count == -1:
                    return False
            return left_count == 0

        answer = []
        from collections import deque
        queue = deque([""])

        while queue:
            cur_str = queue.popleft()

            if len(cur_str) == 2*n :
                if isValid(cur_str):
                    answer.append(cur_str)
                # print(cur_str, 'queue in the 2n loop -> ', queue)
                # the following continue instruction is very important, because it ends the while loop
                # and continues on next iteration because eventually, all the strings in the queue will
                # have a length of 2n and this will keep the queue popping out all its contents
                # without receiving any more strings and eventually the condition of the while 
                # loop will be unsatisfied and the loop would stop and the answer returned.
                continue

            queue.append(cur_str+')')
            queue.append(cur_str+'(')
            # print(cur_str, 'queue outside -> ', queue)

        return answer



sol = Solution()
print(sol.generateParenthesis(2))