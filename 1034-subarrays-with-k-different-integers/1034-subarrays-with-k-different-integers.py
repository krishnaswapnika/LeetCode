class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostk(nums,k):
            l =0
            dic = {}
            ans = 0
            val = 0
            for r in range(len(nums)):
                val = nums[r]
                if val in dic:
                    dic[val] += 1
                else:
                    dic[val] =1
                while len(dic) > k :
                    lval = nums[l]
                    dic[lval] -= 1
                    if dic[lval] == 0:
                        dic.pop(lval)
                    l += 1
                ans += r-l+1
            return ans
        ans = atmostk(nums,k) - atmostk(nums, k-1)
        return ans



