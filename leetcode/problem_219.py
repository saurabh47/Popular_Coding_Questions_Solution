### Problem 219. Contains Duplicate II (Easy): https://leetcode.com/problems/contains-duplicate-ii/

# Tags : Array, Hash Table
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        fr = {}
        for i in range(len(nums)):
            if(nums[i] not in fr):
                fr[nums[i]] = i
            else:
                if(abs(i-fr[nums[i]]) <= k):
                    return True
                else:
                    fr[nums[i]] = i
        return False
