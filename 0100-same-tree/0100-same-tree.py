# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(pe,qe):
            if not pe and not qe:
                return True
            if not pe or not qe or pe.val!=qe.val:
                return False
            left = dfs(pe.left,qe.left)
            right = dfs(pe.right,qe.right)
            
            return (left and right)
        return dfs(p,q)