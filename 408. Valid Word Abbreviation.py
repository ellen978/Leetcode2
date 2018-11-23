'''
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
'''

class Solution:
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        word+='a'
        abbr+='a'
        alpha_abbr=[x for x in abbr if x.isalpha() and x not in word]
        if len(alpha_abbr)>0:
            return False
        else:
            i=0
            while i<len(abbr):
                if abbr[i].isalpha():
                    if abbr[i]==word[i]:
                        i+=1
                    else:
                        return False
                else:
                    digit=abbr[i+1:].index([x for x in abbr[i+1:] if x.isalpha()][0])
                    num=abbr[i:i+digit+1]
                    if num[0]=='0':
                        return False
                    elif i+int(num)<len(word):
                        word=word[:i]+num+word[i+int(num):]
                        i+=digit+1
                    else:
                        return False
            return word==abbr
