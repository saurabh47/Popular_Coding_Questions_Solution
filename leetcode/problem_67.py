### Problem 67. Add Binary (Easy): https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = ''
        while(i >= 0 or j >= 0 or carry):
            if(i >= 0):
                carry += int(a[i])
                i -= 1
            if(j >= 0):
                carry += int(b[j])
                j -= 1
            # carry can be either 0 or 1
            result = str(carry % 2 ) + result
            carry //=2
        return result