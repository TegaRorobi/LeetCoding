#include <iostream> 
#include <string>
#include <vector>

using std::cout;
using std::string;
using std::vector;
using std::endl;
using std::min;

string longestCommonPrefix1(vector<string> strs){
	string lcp = strs[0];

	for(string s:strs){
		string common = "";
		for (short i = 0; i < min(lcp.length(), s.length()); ++i){
			if (s[i] == lcp[i]){
				common += s[i];
			} else break;
		}
		lcp = common;
	}
	return lcp;
}

string longestCommonPrefix(vector<string> strs){
	string lcp;
	for (int i=0; i<strs[0].size(); ++i){
		char chr = strs[0][i];
		for (const string s:strs){
			if (chr != s[i])
				return lcp;
		}
		lcp += chr;
	}
	return lcp;
}

int main(){
	cout << longestCommonPrefix(vector<string>{"flower","flow","flight"}) << endl;
	cout << longestCommonPrefix(vector<string>{"ab", "a"}) << endl;
	vector<string> testcase(1000, "flower");
	testcase.push_back("xylophone");
	cout << longestCommonPrefix1(testcase) << endl;

	cout << "C++ Standard version: " << __cplusplus << endl;
	return 0;
}