# Problem 237. Delete Node in a Linked List (Medium): https://leetcode.com/problems/delete-node-in-a-linked-list/description/

# hint:You are not supposed to deletet the node as mentioned in the problem statement.
class Solution:
    def deleteNode(self, node):
        prev = None
        while(node.next):
            node.val = node.next.val
            prev = node
            node = node.next
        prev.next = None

