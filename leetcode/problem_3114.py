### Problem 3114. Latest Time You Can Obtain After Replacing Characters (Easy): https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        if(s[0] == '?' and s[1] == '?'):
            s[0] = '1'
            s[1] = '1'
        elif(s[0] == '?' and int(s[1]) < 2 ):
            s[0] = '1'
        elif(s[0] == '?' and int(s[1]) > 1 ):
            s[0] = '0'
        elif(s[0] == '0' and s[1] == '?'):
            s[1] = '9'
        elif(s[0] == '1' and s[1] == '?'):
            s[1] = '1'

        if(s[3] == '?'):
            s[3] = '5'
        if(s[4] == '?'):
            s[4] = '9'
        return "".join(s)