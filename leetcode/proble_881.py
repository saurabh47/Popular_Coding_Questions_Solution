### Problem 881. Boats to Save People (Medium): https://leetcode.com/problems/boats-to-save-people/
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        folks = sorted(people)
        start = 0
        end = len(folks) - 1
        boats = 0
        # [1, 2, 2, 3]
        # [3, 3, 4, 5]
        while(start <= end):
            if(folks[start] + folks[end] <= limit):
                start += 1
            end -= 1
            boats += 1
        return boats

            