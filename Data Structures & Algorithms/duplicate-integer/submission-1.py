class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # approach 1 using hashset
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False

        # approach 2 using sorting
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True
        return False