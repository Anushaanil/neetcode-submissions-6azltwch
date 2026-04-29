from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        s_map = Counter(s)
        t_map = Counter(t)

        for letter in s:
            if len(s_map) != len(t_map):
                return False
                
            if letter not in t_map:
                return False

            if s_map[letter] != t_map[letter]:
                return False

        return True
            
