class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                nse = i
                element = stack.pop()
                pse = stack[-1] if stack else -1
                max_area = max(max_area, heights[element]*(nse-pse-1))
            stack.append(i)

        while stack:
            nse = n
            element = stack.pop()
            pse = stack[-1] if stack else -1
            max_area = max(max_area, heights[element]*(nse-pse-1))
            
        return max_area