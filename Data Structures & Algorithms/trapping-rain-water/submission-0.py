class Solution:
    def trap(self, height: List[int]) -> int:
        # approach 1 using left and right max list
        # O(n), O(n)
        if not height:
            return 0
            
        n = len(height)
        l_max = [height[0]]*n
        r_max = [height[-1]]*n
        total = 0

        for i in range(1, n):
            l_max[i] = max(height[i], l_max[i-1])

        for j in range(n-2, -1, -1):
            r_max[j] = max(height[j], r_max[j+1])
        
        for h in range(n):
            if ((height[h] < l_max[h]) and (height[h] < r_max[h])):
                total+=min(l_max[h], r_max[h])-height[h]

        return total