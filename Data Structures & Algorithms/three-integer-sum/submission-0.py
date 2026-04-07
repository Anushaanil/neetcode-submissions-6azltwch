class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # Optimization: as we sort the elements, 
            # elements > 0 and it's after elements could never produce 0
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue # To avoid duplicate triplets, skip 'nums[i]' if it's the same as the previous number.

            left = i + 1
            right = n - 1
            target = -(nums[i])
        
            while left < right:
                sum_ele = nums[left] + nums[right]

                if sum_ele == target:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left+=1 

                    while left < right and nums[left] == nums[left-1]:
                        left+=1 # To avoid duplicate 'nums[l, r]' pairs, skip 'l' if it’s the same as the previous number.

                elif sum_ele > target:
                    right-=1

                else:
                    left+=1

        return triplets
