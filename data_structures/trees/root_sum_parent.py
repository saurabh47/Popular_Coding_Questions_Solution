### Problem from Geeks for Geeks
### https://www.geeksforgeeks.org/problems/children-sum-parent/1
class Solution:
    #Function to check whether all nodes of a tree have the value
    #equal to the sum of their child nodes.
    def isSumProperty(self, root):

        if(root is None or (root.left is None and root.right is None)):
            return 1
        left_sum = 0
        right_sum = 0
        if(root.left):
            left_sum = root.left.data
        if(root.right):
            right_sum = root.right.data
        if((root.data == left_sum + right_sum) and self.isSumProperty(root.left) and self.isSumProperty(root.right)):
            return 1
        else:
            return 0