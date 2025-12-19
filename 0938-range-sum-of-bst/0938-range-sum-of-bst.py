# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #if node is greater than low then only move to right
        # then check everynode and if they are low or right
        # sum the nodes between those ranges.
        res = 0
        def dfs(node):
            if not node:
                return 0
            if node.val>high:
                return(dfs(node.left))
            if node.val<low:
                return(dfs(node.right))
            
            return node.val+ dfs(node.left)+dfs(node.right)

        return dfs(root)

        

        