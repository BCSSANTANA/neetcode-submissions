class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = (m * n) - 1
        c = (l + r) // 2
        leftIdxs = self.getIndexes(m, n, l)
        rightIdxs = self.getIndexes(m, n, r)
        centerIdxs = self.getIndexes(m, n, c)
        if matrix[leftIdxs[0]][leftIdxs[1]] == target or matrix[rightIdxs[0]][rightIdxs[1]] == target or matrix[centerIdxs[0]][centerIdxs[1]] == target:
                return True
        while l < r:
            c = (l + r) // 2
            leftIdxs = self.getIndexes(m, n, l)
            rightIdxs = self.getIndexes(m, n, r)
            centerIdxs = self.getIndexes(m, n, c)
            if matrix[leftIdxs[0]][leftIdxs[1]] == target or matrix[rightIdxs[0]][rightIdxs[1]] == target or matrix[centerIdxs[0]][centerIdxs[1]] == target:
                return True
            elif target < matrix[centerIdxs[0]][centerIdxs[1]]:
                r = c - 1
            else:
                l = c + 1
        return False

    
    def getIndexes(self, m: int, n: int, num: tuple[int, int]) -> List[int, int]:
        res = [0] * 2
        res[0] = num // n
        res[1] = num % n
        return res