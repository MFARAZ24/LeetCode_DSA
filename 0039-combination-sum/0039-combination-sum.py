class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curCom = []
        def dfs(index, curSum, curCom):

            if curSum == target:
                res.append(curCom)
                return
            
            
            if index>=len(candidates) or curSum>target:
                return 
            for i in range(index, len(candidates)):
            
                dfs(i,curSum+candidates[i],curCom+[candidates[i]])
            
        dfs(0,0,[])
        return res