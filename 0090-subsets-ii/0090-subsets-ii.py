class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, subset):
            if index>len(nums):
                return
            if index==len(nums):
                res.append(subset)
                return
            
            dfs(index+1,subset+[nums[index]])
            while index+1<len(nums) and nums[index] == nums[index+1]:
                index = index+1
            dfs(index+1,subset)
        dfs(0,[])
        return res

        
        