class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in range(len(matrix)):
            l = 0
            r = len(matrix[0]) - 1

            if matrix[row][l] <= target <= matrix[row][r]:
                while l <=r:
                    m = (l+r)//2
                    if matrix[row][m] == target:
                        return True

                    elif matrix[row][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
        return False
