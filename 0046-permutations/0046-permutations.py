class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            if index==len(nums):
                return
            for n in nums:
                if n in perm:
                    continue
                dfs(perm + [n])
            
        dfs([])

        return res