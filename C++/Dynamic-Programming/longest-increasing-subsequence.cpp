#include <iostream>
#include <vector>

using std::vector;

int lengthOfLIS(vector<int> nums) {
	int numsLength = nums.size();

	vector<int> dp(numsLength-1, 0);
	// base case
	dp.push_back(1);

	for (int i=numsLength-2; i>-1; --i)
		for (int j=i+1; j<numsLength; ++j) 

			if (nums[j] > nums[i])
				dp[i] = std::max(dp[i], 1+dp[j]);

	// just returning the maximum of the dp array
	int ans = 0;
	for (int n:dp)
		ans = std::max(ans, n);

	return ans;
}

int main() {
	vector<int> nums = {5, 7, -2, 0, -1, 8, 1, 2, 4};
	std::cout << lengthOfLIS(nums);
}