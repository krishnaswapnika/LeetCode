class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def fun(dica,dicb):
            if len(dica) != len(dicb):
                return False
            for i in dica:
                if i not in dicb or dica[i] != dicb[i]:
                    return False
            return True
        
        dica = {}
        dicb = {}
        n = len(p)
        for i in p:
            if i in dicb:
                dicb[i] += 1
            else:
                dicb[i] = 1

        l = 0
        ans = []       
        for r in range(len(s)):
            val = s[r]
            if val in dica:
                dica[val] += 1
            else:
                dica[val] = 1

            if r-l == n:
                dica[s[l]] -= 1
                if dica[s[l]] == 0:
                    dica.pop(s[l])
                l += 1
        
            if r-l+1 == n:
                if fun(dica,dicb):
                    ans.append(l)
        return ans 

            

