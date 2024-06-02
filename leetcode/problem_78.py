# hint: https://www.youtube.com/watch?v=h4zNvA4lbtc

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # power set of an array consists of 2^n
        # so we can consider set bits in binary
        size = len(nums)
        for i in range(1 << size):
            subset = []
            for j in range(size):
                # check if bit is set by AND with i
                if((1 << j) & i):
                    subset.append(nums[j])
            result.append(subset)
        return result