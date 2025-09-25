class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        t= 0
        if sum(gas) < sum(cost):
            return -1
        s = 0
        t= 0
        for i in range(len(gas)):
            t += gas[i] - cost[i]
            if t < 0:
                s = i + 1
                t= 0  
        return s