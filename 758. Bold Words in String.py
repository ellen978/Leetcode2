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
