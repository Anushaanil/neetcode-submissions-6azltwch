class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            
            if diff in num_map:
                if num_map[diff] < i:
                    return [num_map[diff], i]
                else:
                    return [i, num_map[diff]]
            else:
                num_map[nums[i]] = i
                    
