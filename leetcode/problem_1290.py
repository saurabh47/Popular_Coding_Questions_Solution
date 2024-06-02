## Problem 1290. Convert Binary Number in a Linked List to Integer (Easy): https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count =-1
        temp = head
        result = 0
        while(temp):
            temp = temp.next
            count += 1
        temp = head
        while(temp):
            # result += temp.val* (2 ^ count)
            result += (temp.val << count)
            temp = temp.next
            count -=1 
        return result
        

# Time complexity: O(n)
# Space complexity: O(1)

if __name__ == '__main__':
    s = Solution()
    print(s.getDecimalValue([1,0,1])) # 5
    print(s.getDecimalValue([0])) # 0
    print(s.getDecimalValue([1])) # 1
    print(s.getDecimalValue([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])) # 18880
    print(s.getDecimalValue([0,0])) # 0
    print(s.getDecimalValue([1,0,1,1])) # 11
    print(s.getDecimalValue([0,1,0])) # 2
    print(s.getDecimalValue([1,0,0,1,0,0,0,0,0,0,0])) # 11264
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0])) # 1024
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0,0])) # 2048
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0,0,0])) # 4096
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0,0,0,0])) # 8192
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) # 16384
    print(s.getDecimalValue([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])) # 32768