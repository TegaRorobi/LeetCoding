# include <iostream>
# include <vector>

using std::vector;

int coinChange(vector<int>coins, int amount) {
	vector<int> dp (amount+1, amount+1);
	dp[0] = 0;
	// i could just use an integer pointer to the indices of the 
	// dp array, but I just decided to use an iterator for the fun of it.
	for (auto it=dp.begin()+1; it < dp.end(); ++it) 
		for (int coin: coins)
			if (it-coin >= dp.begin())
				*it = std::min(*it, 1+*(it-coin));

	return *(dp.end()-1) != amount+1? *(dp.end()-1) : -1;
}

int main() {
	std::cout << coinChange(vector<int>{1, 3, 4, 5}, 7);
	return 0;
}