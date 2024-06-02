### Problem 42. Trapping Rain Water (Hard): https://leetcode.com/problems/trapping-rain-water/
### Tags: Array, Two Pointers, Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for i in range(len(height))]
        right_max = [0 for i in range(len(height))]
        water_collected = 0

        # create a array to store left max at i
        max_l = height[0]
        for i in range(len(height)):
            if(max_l < height[i]):
                max_l =  height[i]
            left_max[i] = max_l
        # create a array to store right max at i
        max_r = height[-1]
        for i in range(len(height) -1, -1, -1):
            if(max_r < height[i]):
                max_r = height[i]
            right_max[i] = max_r
        # calculate the water collected at i
        for i in range(len(height)):
            h = height[i]
            water_collected += min(left_max[i], right_max[i]) - h
        return water_collected