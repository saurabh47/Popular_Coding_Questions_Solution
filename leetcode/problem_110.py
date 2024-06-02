### Problem 110. Balanced Binary Tree (Easy): https://leetcode.com/problems/balanced-binary-tree/
# hint: Perform inorder tarversal and check for each node if depth is greater than 1
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True
        stack = []
        if(root is None):
            return True
        while(True):
            while(root):
                stack.append(root)
                root = root.left
            if(not stack):
                break
            root = stack.pop()
            hl = self.height(root.left)
            hr = self.height(root.right)
            if(abs(hl - hr) > 1):
                return False
            root = root.right
        return ans
    
    def height(self, root: TreeNode)->int:
        if(root is None):
            return 0
        else:
            return max(self.height(root.left), self.height(root.right)) + 1