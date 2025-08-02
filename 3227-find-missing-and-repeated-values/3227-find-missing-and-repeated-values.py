class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=[]
        c=0
        for i in grid:
            for j in i :
                if j in l:
                    c=j
                else:
                    l.append(j)
        a=min(l)
        b=max(l)
        res=[]
        m=0
        for i in range(1,b+1):
            if i not in l:
                m=i
                break
        if m==0:
            if b+1 not in l:
                m=b+1
        res.append(c)
        res.append(m)
        return res