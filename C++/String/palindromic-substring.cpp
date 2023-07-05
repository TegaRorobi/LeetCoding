
#include <iostream>

using namespace std;


class Solution {
public:

	int extendPalindrome(string s, int l, int r) {
		int count = 0;
		while (l>=0 && r < s.length() && s[l] == s[r]){
			++count; --l; ++r;
		}
		return count;
	}

	int countSubstrings(string s) {

		int count = 0;
		for(int i=0; i<s.length(); ++i) {
			count += extendPalindrome(s, i, i);
			count += extendPalindrome(s, i, i+1);
		}
		return count;
	}

	int countSubstrings2(string s) {
		int count = 0, n=s.length();
		for (int i=0; i<n; ++i) {
			for (int l=i,r=i;   l>=0 && r<n && s[l]==s[r]; l--,r++) 
				count++;
			for (int l=i,r=i+1; l>=0 && r<n && s[l]==s[r]; l--,r++) 
				count++;
		}
		return count;
	}
};




int main(){
	Solution a;
	cout << a.countSubstrings2("aaa") << endl;
	cout << a.countSubstrings2("abc") << endl;
	return 0;
}