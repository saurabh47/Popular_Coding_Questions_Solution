### Problem 2265. Count Nodes Equal to Average of Subtree (Medium): https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

### Tags: Tree, Recursion

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        result = 0
        def average(root: TreeNode):
            nonlocal result
            if(root is None):
                return (0, 0)
            left_pair = average(root.left)
            right_pair = average(root.right)
            count = 1 + left_pair[1] + right_pair[1]
            sum_n = root.val + left_pair[0] + right_pair[0]
            avg = (sum_n // count)

            if(avg == root.val):
                result += 1
            return (sum_n, count)

        average(root)
        return result