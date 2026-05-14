class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        unique_set = set()

        while r < len(s):
            while s[r] in unique_set:
                unique_set.remove(s[l])
                l+=1
                
            unique_set.add(s[r])
            
            max_len = max(max_len, r-l+1)
            r+=1
        return max_len