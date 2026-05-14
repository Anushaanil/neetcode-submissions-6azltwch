class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_map = {}
        s2_map = {}

        for r in range(len(s1)):
            s1_map[s1[r]] = s1_map.get(s1[r], 0) + 1

        for r in range(len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            
            if (r-l+1) > len(s1):
                s2_map[s2[l]] -=1

                if s2_map.get(s2[l],0) == 0:
                    del s2_map[s2[l]]
                
                l+=1

            if s1_map == s2_map:
                return True

        return False