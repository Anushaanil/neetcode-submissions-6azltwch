class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = sorted(nums1+nums2)
        # even length
        n = len(sorted_arr)
        if n % 2 == 0:
            mid_index = n//2
            return (sorted_arr[mid_index-1] + sorted_arr[mid_index])/2
        return sorted_arr[n//2]