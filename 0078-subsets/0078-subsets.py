class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, subset):
            if index>= len(nums):
                return res.append(subset.copy())

            subset.append(nums[index])

            dfs(index+1, subset)
            subset.pop()
            dfs(index+1,subset)
        dfs(0,[])
        return res