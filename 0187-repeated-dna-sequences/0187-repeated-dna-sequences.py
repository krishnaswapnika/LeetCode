class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        k = 10
        n = len(s)
        ans = []
        dic = {}
        if n < k:
            return []
        for i in range(n-k+1):
            val = s[i:i+k]
            if val in dic:
                dic[val] += 1
            else:
                dic[val] = 1
        for r in dic:
            if dic[r] > 1:
                ans.append(r)
        return ans


