class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        if s == t:
            return s
        
        t_char_freq_map = {}
        for char in t:
            t_char_freq_map[char] = t_char_freq_map.get(char,0) + 1

        required = len(t_char_freq_map)
        formed = 0
        window_map = {}

        l = 0
        res_len = float("inf")
        res = ""

        for r in range(len(s)):
            char = s[r]
            window_map[char] = window_map.get(char,0) + 1
            
            if (char in t_char_freq_map 
                and window_map[char] == t_char_freq_map[char]
            ):
                formed+=1

            while required == formed:
                window_len = r-l+1
                if window_len < res_len:
                    res_len = window_len
                    res = s[l:r+1]

                left_char = s[l]
                window_map[left_char] -=1

                if (
                    left_char in t_char_freq_map 
                    and window_map[left_char] < t_char_freq_map[left_char]
                ):
                    formed-=1
                l+=1
        return res