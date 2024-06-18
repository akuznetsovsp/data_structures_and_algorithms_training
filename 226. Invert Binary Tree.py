# https://leetcode.com/problems/invert-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if root.left is None and root.right is None:
            return root

        root = TreeNode(root.val, left=root.right, right=root.left)
        print(root)
        return root


# Tests
# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

# Input: root = [2,1,3]
# Output: [2,3,1]

# Input: root = []
# Output: []
