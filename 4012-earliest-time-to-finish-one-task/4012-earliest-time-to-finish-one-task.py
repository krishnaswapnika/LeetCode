class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        f= [s+t for s, t in tasks]
        return min(f)
