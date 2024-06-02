### Problem 191. Number of 1 Bits (Easy): https://leetcode.com/problems/number-of-1-bits/
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if((1 << i) & n):
                count += 1
        return count