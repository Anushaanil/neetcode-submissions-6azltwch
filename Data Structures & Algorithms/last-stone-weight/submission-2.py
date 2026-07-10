import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using -ve numbers property to implement max heap
        self.heap = [-1 * val for val in stones]
        
        # continue the loop until we have elements in heap
        while len(self.heap) > 1:
            heapq.heapify(self.heap)
            # can't access it via indices like this because heap 
            # is not sorted array, 1st ele will be smallest but we can't say
            # 2nd is sorted as well here
            # pop the 2 largest anyways in any condition

            x = heapq.heappop(self.heap)
            y = heapq.heappop(self.heap)

            # if val is lesser than push the difference
            if x < y:
                heapq.heappush(self.heap, x-y)

        # return by multiplying the final ans with -1 to get the ideal answer  
        return -1 * self.heap[0] if self.heap else 0