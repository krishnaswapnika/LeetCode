class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        chosen = set()
        num = 1
        total = 0
        while len(chosen)<n:
            if (k-num) not in chosen:
                chosen.add(num)
                total+=num
            num+=1
        return total