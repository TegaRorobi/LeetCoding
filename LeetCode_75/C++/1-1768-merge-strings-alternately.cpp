/*
Problem Statement:
------------------
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating
    order, starting with word1. If a string is longer than the other, append the additional letters
    onto the end of the merged string.

    Return the merged string.

Approach:
---------
    For this solution, I'll traverse both strings, with index pointers, up to the point of the shortest
    string. At the end of this, I'll add the remaining letters from the longer string if any.

Complexity:
-----------
    Time: O(m+n) => We traverse the strings only once
    Space: O(1)
*/

#include <iostream>

class Solution {
public:
    std::string mergeAlternately (std::string word1, std::string word2) {
        std::string res;
        short i;
        for (; i<std::min(word1.size(), word2.size()); i++) {
            res += word1[i];
            res += word2[i];
        }
        res.insert(res.end(), word1.begin()+i, word1.end());
        res.insert(res.end(), word2.begin()+i, word2.end());

        return res;
    }
};

int main() {
    Solution soln;
    std::cout << soln.mergeAlternately("abcde", "fgh") << std::endl;
    return 0;
}