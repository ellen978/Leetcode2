'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
'''

class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        odd=0
        s_list=list(set(s))
        i=0
        while i<len(s_list):
            if s.count(s_list[i])%2==1:
                odd+=1
            i+=1
        return odd<=1
