import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l<r:
            m = (l+r)//2
            eating_speed = sum(math.ceil(i/m) for i in piles)

            if eating_speed <= h:
                r = m
            else:
                l = m + 1
                
        return r