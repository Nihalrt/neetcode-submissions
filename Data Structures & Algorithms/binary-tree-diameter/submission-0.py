# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def DFS_travel(node):
            if not node:
                return 0
            
            left = DFS_travel(node.left)
            right = DFS_travel(node.right)

            current = left+right
            self.max_diameter = max(self.max_diameter, current)

            return max(left, right) + 1
        
        DFS_travel(root)
        return self.max_diameter



        