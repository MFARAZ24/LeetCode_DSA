class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #operations = int(operations)
        res = []
        if len(operations)<2:
            return None
        for i in range(len(operations)):
            if operations[i] == "C":
                res.pop()
            elif operations[i] =="+":
                res.append(res[-1] + res[-2])
            elif operations[i] == "D":
                res.append(res[-1]*2)
            else:
                res.append(int(operations[i]))
        return sum(res)
        