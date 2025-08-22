class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rowLeft, rowRight = 0, len(matrix)
        index = -1
        while rowLeft <= rowRight:
            mid = (rowLeft + rowRight) // 2
            if target < matrix[mid][0]:
                rowRight = mid - 1
            elif target > matrix[mid][-1]:
                rowLeft = mid + 1
            else:
                index = mid
                break

        if index == -1: return False
        
        left, right = 0, len(matrix[0])
        while left <= right:
            mid = (left + right) // 2

            if target < matrix[index][mid]:
                right = mid - 1
            elif target > matrix[index][mid]:
                left = mid + 1
            else:
                return True

        return False
