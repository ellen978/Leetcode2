'''
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
'''

class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        S_lower=S
        for x in words:
            if x in S_lower:
                S_alt=S_lower
                shift=0
                while x in S_alt:
                    index=S_alt.index(x)
                    S=S[:index+shift]+S[index+shift:index+shift+len(x)].upper()+S[index+shift+len(x):]
                    S_alt=S_alt[index+1:]
                    shift+=index+1
        S='+'+S+'+'
        S_lower='+'+S_lower+'+'
        i=0
        while i<len(S)-1:
            if S[i]==S_lower[i] and S[i+1]!=S_lower[i+1]:
                S=S[:i+1]+'<b>'+S[i+1:]
                S_lower=S_lower[:i+1]+'<b>'+S_lower[i+1:]
                i+=4
            elif S[i]!=S_lower[i] and S[i+1]==S_lower[i+1]:
                S=S[:i+1]+'</b>'+S[i+1:]
                S_lower=S_lower[:i+1]+'</b>'+S_lower[i+1:]
                i+=5
            else:
                i+=1
        return S_lower[1:len(S_lower)-1]
