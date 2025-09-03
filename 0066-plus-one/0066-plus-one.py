class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        res = num + 1
        ans = list(map(int, str(res)))
        return ans