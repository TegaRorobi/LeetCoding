
# include <iostream>
# include <vector>
# include <string>
# include <math.h>

using std::cout;
using std::endl;
using std::string;
using std::max;
// using std::vector;

class Solution {

public:
	// this get's called when a new class is instantiated
	Solution() { cout << "Entry..." << endl; }

	// the method we set up a whole class for
	int longestCommonSubsequence(string text1, string text2) {

		int m = text1.size(), n = text2.size();
		int dp[m+1][n+1] = {};

		for (int i = 1; i <= m; ++i){
			for (int j = 1; j <= n; ++j){

				if (text1[i-1] == text2[j-1]) dp[i][j] = 1+dp[i-1][j-1] ;
				else dp[i][j] = max(dp[i-1][j], dp[i][j-1]) ;

			}
		}
		return dp[m][n];
	}


	// this get's called when the class is destroyed or at the end of runtime
	~Solution() { cout << "Exit." << endl; }
	
};


int main()
{
	Solution soln;
	string txt1 = "abcde";
	string txt2 = "abc";
	cout << "Length of longest common subsequence between \"" 
		<< txt1 << "\" and \"" << txt2 << "\" is "
		<< soln.longestCommonSubsequence(txt1, txt2) << endl;
}


