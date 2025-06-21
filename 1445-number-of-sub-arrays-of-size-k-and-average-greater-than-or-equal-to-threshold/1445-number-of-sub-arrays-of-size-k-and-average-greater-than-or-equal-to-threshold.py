class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        l = 0
        temp = 0
        c = 0
        for r in range(n):
            temp += arr[r]
            if r-l == k:
                temp -= arr[l]
                l+=1
            if r-l+1 == k:
                if (temp/k)>= threshold:
                    c+= 1
        return c