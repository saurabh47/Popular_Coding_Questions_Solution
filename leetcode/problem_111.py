### Problem 111. Minimum Depth of Binary Tree (Easy): https://leetcode.com/problems/minimum-depth-of-binary-tree/

# hint: run a level order traversal and return the depth when you find a leaf node
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if(root is None):
            return depth
        q.append(root)
        while(True):
            size = len(q)
            if(size == 0):
                return depth
            depth += 1
            while(size > 0):
                top = q.popleft()
                if((top.left is None) and (top.right is None)):
                    q = deque()
                    break
                if(top.left):
                    q.append(top.left)
                if(top.right):
                    q.append(top.right)
                size -= 1
        return depth
