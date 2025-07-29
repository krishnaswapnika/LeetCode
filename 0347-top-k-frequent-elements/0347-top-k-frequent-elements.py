from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        return [item for item, freq in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

