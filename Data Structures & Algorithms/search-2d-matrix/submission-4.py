class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = self.indicesToIndex(cols, rows - 1, cols - 1)

        while low <= high:
            mid = (low + high) // 2
            midIndices = self.indexToIndices(cols, mid)
            if matrix[midIndices[0]][midIndices[1]] == target:
                return True
            elif  matrix[midIndices[0]][midIndices[1]] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False               





    def indicesToIndex(self, cols: int, x: int, y: int) -> int:
        return x * cols + y 


    def indexToIndices(self, cols: int, ind: int) -> Tuple[int, int]:
        row = ind//cols             
        return (row, (ind - (cols * row))) 