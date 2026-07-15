class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ### using a set ###
        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return num
        #     seen.add(num)

        # modifying list to find duplicate
        # for num in nums:
        #     index = abs(num) - 1

        #     if nums[index] < 0:
        #         return abs(num)

        #     nums[index] *= -1
        
        # using fast and slow pointers
        # Phase 1: Find intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find entrance of cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
