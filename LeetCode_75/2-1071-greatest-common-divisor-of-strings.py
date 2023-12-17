"""
Problem Statement:
------------------
    For two strings s and t, we say "t divides s" if and only if s = t + ... + t
    (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Approach:
---------
    For this solution, we know that for there to be a common divisor for the strings, then the
    following condition must be met:

        str1 + str2 == str2 + str1

    Therefore, if this is true, then we have a gcd, and if not, we can return an empty string ""
    The GCD for the strings is essentially a particular prefix multiplied a certain number of times.
    So, to get the GCD of the strings, we can get the GCD number of the lengths of the strings, and
    then use that to determine the string GCD prefix.

Complexity:
-----------
    Time: O(m+n) => We traverse the strings only once
    Space: O(1)
"""


class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        # this module will calculate the gcd number from the length, and we
        # simply return a prefix of any of the strings, with that length
        from math import gcd
        l1, l2 = len(str1), len(str2)
        return str1[:(gcd(l1, l2))]


    # iterative GCD from factors
    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""

        l1, l2 = len(str1), len(str2)

        l = l1 if l1 < l2 else l2 # min(l1, l2)

        factors = [l/x for x in range(2, l+1)] # the larger factors would come first

        for factor in factors:
            # make sure this is a common factor
            if l1 % factor or l2 % factor:
                continue

            substr = str1[:factor] # a possible GCD prefix string

            # l1//factor represents the number of times the prefix is multiplied to produce str1
            if str1==substr*(l1//factor) and str2==substr*(l2//factor):
                return substr


    # recursive approach
    def gcdOfStrings3(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) == len(str2):
            return str1

        if len(str1) > len(str2):
            return self.gcdOfStrings3(str1[len(str2):],str2)

        else:
            return self.gcdOfStrings3(str1,str2[len(str1):])




soln = Solution()
print(
    soln.gcdOfStrings('ABABAB', 'ABAB'),
    soln.gcdOfStrings('ABCABCABCABC', 'ABCABCABC'),
    soln.gcdOfStrings('ABCDEF', 'DEF'),
)

print(
    soln.gcdOfStrings2('ABABAB', 'ABAB'),
    soln.gcdOfStrings2('ABCABCABCABC', 'ABCABCABC'),
    soln.gcdOfStrings2('ABCDEF', 'DEF'),
)

print(
    soln.gcdOfStrings3('ABABAB', 'ABAB'),
    soln.gcdOfStrings3('ABCABCABCABC', 'ABCABCABC'),
    soln.gcdOfStrings3('ABCDEF', 'DEF'),
)
