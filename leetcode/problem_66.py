### Problem 66. Plus One (Easy): https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for n in digits:
            num  = num * 10 + n
        num = num + 1
        res = [int(x) for x in str(num)]
        return res