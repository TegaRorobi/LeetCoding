class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # also works, but with more memory
        # hashmap = {0:0, 1:0, 2:0}
        # for n in nums:
        #     hashmap[n]+=1
        # pos_sum = 0
        # for key, value in hashmap.items():
        #     nums[pos_sum:] = [key]*value
        #     pos_sum+=value


        # Constant space and linear time solution i.e O(1) space & O(n) time.
        l, r = 0, len(nums)-1
        i = 0

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l+=1
            elif nums[i] == 2:
                swap(i, r)
                r-=1
                i-=1
            i+=1