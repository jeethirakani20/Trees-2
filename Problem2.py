# T.C. O(n)
# S.C. O(h), where h = height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.totalsum = 0
        
    def helper(self, root, curr):
        if root is None:
            return 
        curr = curr * 10 + root.val
        if root.left is None and root.right is None:
            self.totalsum += curr

        self.helper(root.left, curr)
        self.helper(root.right, curr)


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.totalsum
