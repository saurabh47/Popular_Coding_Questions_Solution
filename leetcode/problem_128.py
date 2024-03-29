# Problem 128: Longest Consecutive Sequence (Medium): https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums) -> int:
        # Alternatively we can convert to set
        # and remove the duplicate check
        sortedlist = sorted(nums)
        start = 0
        result = []
        temp = []
        for end in range(len(sortedlist)):
            item = sortedlist[end]
            if(start != end):
                if(abs(item - sortedlist[end-1]) == 1):
                    temp.append(item)
                # Skip duplicate numbers
                # e.g 0 1 1 2
                elif(abs(item - sortedlist[end-1]) == 0):
                    continue
                else:
                    start = end
                    if(len(temp) > len(result)):
                        result = temp.copy()
                    temp.clear()
                    temp.append(item)
            else:
                temp.append(item)
        if(len(temp) > len(result)):
            result = temp.copy()
        return len(result)

if __name__ == "__main__":
    nums = [1,2 ,0, 1]
    print(Solution().longestConsecutive(nums)) # 4
