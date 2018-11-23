'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1=[i for i in range(len(words)) if words[i]==word1]
        index2=[i for i in range(len(words)) if words[i]==word2]
        ret_min=float('inf')
        i=0
        while i<len(index1):
            j=0
            while j<len(index2):
                if abs(index2[j]-index1[i])<ret_min:
                    ret_min=abs(index2[j]-index1[i])
                j+=1
            i+=1
        return ret_min
