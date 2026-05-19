from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_dq = deque()
        res = []

        if k == 1:
            return nums

        if k == len(nums):
            return [max(nums)]

        for r in range(len(nums)):
            # check if we are within k elements range
            if nums_dq and nums_dq[0] <= r-k:
                nums_dq.popleft()

            # remove smaller elements at back
            while nums_dq and nums[nums_dq[-1]] <= nums[r]:
                nums_dq.pop()

            nums_dq.append(r)
            # append once we cross the limit value k
            if r >= k-1:
                res.append(nums[nums_dq[0]])

        return res