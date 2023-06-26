
# include <iostream>
using std::cout;

int uniquePaths(int m, int n)
{
	int dp[n+1];
	// populate the dp array with zeros
	for (int i = 0; i <= n; ++i) dp[i]= (i==n-1)?1:0;

	for (int r=m-1; r>=0; --r) {

		for(int c=n-1; c>=0; --c) 
			dp[c] = dp[c+1]+dp[c];
	}
 
 	return dp[0];
}


int main()
{
	cout << uniquePaths(3, 7);
	return 0;
}
