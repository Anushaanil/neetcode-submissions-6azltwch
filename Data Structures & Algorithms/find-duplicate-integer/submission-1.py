class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ### using a set ###
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                return abs(num)

            nums[index] *= -1
