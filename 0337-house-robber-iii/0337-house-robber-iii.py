# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return[0,0]

            leftroot = dfs(node.left)
            rightroot = dfs(node.right)
            withRoot = node.val+leftroot[1]+rightroot[1]
            withoutRoot = max(leftroot) + max(rightroot)
            return [withRoot,withoutRoot]

        return max(dfs(root))
        
        