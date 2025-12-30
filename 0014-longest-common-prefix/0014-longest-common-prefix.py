class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        fw = strs[0]
        res = 0

        for r in range(len(fw)):
            pre = fw[0:r+1]
            for s in strs:
                if pre != s[0:r+1]:
                    return fw[0:res]

            res=res+1

        return fw[0:res]
        