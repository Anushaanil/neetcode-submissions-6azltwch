class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count_map = {}
        max_freq = 0
        res = 0

        while r < len(s):
            count_map[s[r]] = count_map.get(s[r], 0) + 1
            
            max_freq = max(max_freq, count_map[s[r]])

            while ((r-l+1) - max_freq) > k:
                count_map[s[l]]-=1
                l+=1

            res = max(res, r-l+1)
            r+=1

        return res