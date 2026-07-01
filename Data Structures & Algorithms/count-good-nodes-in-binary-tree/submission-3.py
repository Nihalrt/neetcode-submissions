# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        queue = deque([(root,root.val)])
        current_max = root.val

        while queue:
            node, current_max = queue.popleft()
            if node.left:
                if node.left.val >= current_max:
                    count+=1
                new_max = max(current_max, node.left.val)
                queue.append((node.left, new_max))
            if node.right:
                if node.right.val >= current_max:
                    count+=1
                new_max = max(current_max, node.right.val)
                queue.append((node.right,new_max))
        return count



        