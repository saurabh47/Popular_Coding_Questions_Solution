### Problem 2236. Root equals sum of children (Easy): https://leetcode.com/problems/root-equals-sum-of-children/
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
       return root.val == (root.left.val + root.right.val)