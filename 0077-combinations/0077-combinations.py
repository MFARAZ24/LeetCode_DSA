class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(index,curr):
            if (len(curr)==k):
                res.append(curr)
                return
            if index>=n:
                return

            for i in range(index+1,n):
                dfs(i,curr+[i+1])
        for i in range(n):
            dfs(i,[i+1])
            
        #dfs(0,[])
        return res