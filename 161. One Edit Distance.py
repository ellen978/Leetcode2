'''
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''

class Solution:
    def isOneEditDistance(self, s, t):
        if abs(len(s)-len(t))>1:
            return False
        elif len(s)==len(t):
            diff=[i for i in range(len(s)) if s[i]!=t[i]]
            if len(diff)==1:
                return True
            else:
                return False
        elif len(s)==len(t)-1:
            if s==t[:len(s)]:
                return True
            else:
                i=0
                while i<len(s):
                    if s[i]==t[i]:
                        i+=1
                    else:
                        s=s[:i]+t[i]+s[i:]
                        break
                return s==t
        elif len(t)==len(s)-1:
            if t==s[:len(t)]:
                return True
            else:
                i=0
                while i<len(t):
                    if t[i]==s[i]:
                        i+=1
                    else:
                        t=t[:i]+s[i]+t[i:]
                        break
                return t==s
