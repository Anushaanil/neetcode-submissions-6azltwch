class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        max_sum, min_sum = nums[0], nums[0]
        cur_max_sum, cur_min_sum = 0, 0
        
        # Kadane for max and min subarry sum
        for num in nums:
            cur_max_sum = max(num, cur_max_sum + num)
            cur_min_sum = min(num, cur_min_sum + num)

            max_sum = max(max_sum, cur_max_sum)
            min_sum = min(min_sum, cur_min_sum)
        
        # edge case when all -ve
        if max_sum < 0:
            return max_sum
        
        return max(max_sum, total_sum - min_sum)