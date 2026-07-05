# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        left_subtree = inorder[0:root_index]
        right_subtree = inorder[root_index+1:]

        left_preorder = preorder[1 : 1 + len(left_subtree)]
        right_preorder = preorder[1 + len(left_subtree) : ]

        root.left = self.buildTree(left_preorder, left_subtree)
        root.right = self.buildTree(right_preorder, right_subtree)
        return root


        