import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # self.heap = nums
        # heapq.heapify(self.heap)

        # while len(self.heap) > k:
        #     heapq.heappop(self.heap)
        
        # return self.heap[0] if self.heap else 0
        
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]