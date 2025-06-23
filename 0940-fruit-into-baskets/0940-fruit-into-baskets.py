class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        l = 0
        ans = 0
        n = len(fruits)
        dic = {}
        for r in range(n):
            if fruits[r] in dic:
                dic[fruits[r]] += 1
            else:
                dic[fruits[r]] = 1
            while len(dic) > k:
                dic[fruits[l]] -= 1
                if dic[fruits[l]] == 0:
                    dic.pop(fruits[l])
                l+=1
            ans = max(ans, r-l+1)
        return ans       


