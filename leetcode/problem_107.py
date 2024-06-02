### Problem 107. Binary Tree Level Order Traversal II (Medium): https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        level_order = []
        if(root is None):
            return level_order
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                return level_order
            data = []
            while(size > 0):
                top = q.popleft()
                data.append(top.val)
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -= 1
            level_order.insert(0,data) 
        return level_order