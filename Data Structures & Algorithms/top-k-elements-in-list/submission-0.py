from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        new_d = dict(sorted(d.items(), key = lambda x:x[1], reverse=True))
        return list(new_d.keys())[:k]