### Problem 543. Diameter of Binary Tree (Easy) https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        if(root is None):
            return diameter
        stack = [root]
        while(True):
            if(not stack):
                break
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            lh = self.height(root.left)
            rh = self.height(root.right)
            diameter = max(lh + rh + 1, diameter)
            root = root.right
        return diameter-1

    def height(self, root:TreeNode) -> int:
        if(root is None):
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1