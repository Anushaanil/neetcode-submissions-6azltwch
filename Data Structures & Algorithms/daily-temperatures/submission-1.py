class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0] * n

        for cur_day in range(n):
            while stack and temperatures[cur_day] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                res[prev_day] = cur_day - prev_day

            stack.append(cur_day)
            
        return res