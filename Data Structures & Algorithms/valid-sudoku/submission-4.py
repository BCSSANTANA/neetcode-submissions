class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        GRID_LEN = 9
        valid_r = set()
        valid_c = set()
        c_i = 0
        i = 0
        j = 0
        while c_i <= 6:
            c_j = 0
            while c_j <= 6:
                if self.check_subbox(i + c_i, j + c_j, GRID_LEN, board, valid_r, valid_c) == False:
                    return False
                c_j += 3
            c_i += 3
        print(valid_r)
        print(valid_c)
        return True

        
    def check_subbox(self, i: int, j: int, GRID_LEN: int, board: List[List[str]], valid_r, valid_c) -> bool:
        c_i = 0
        seen = set()
        while c_i < 3:
            c_j = 0
            if i + c_i not in valid_r:
                if self.row_check(i + c_i, board) == False:
                    return False
                else:
                    valid_r.add(i + c_i)
            while c_j < 3:
                if j + c_j not in valid_c:
                    if self.column_check(j + c_j, board, GRID_LEN) == False:
                        return False
                else:
                    valid_c.add(j + c_j)
                if board[i + c_i][j + c_j] in seen:
                    return False
                elif board[i + c_i][j + c_j] != ".":
                    seen.add(board[i + c_i][j + c_j])
                c_j += 1
            c_i += 1
        return True
    
    def row_check(self, i: int, board: List[List[str]]) -> bool:
        seen = set()
        for elem in board[i]:
            print(elem)
            if elem in seen:
                return False
            elif elem != ".":
                seen.add(elem)
        return True


    def column_check(self, j: int, board: List[List[str]], GRID_LEN: int) -> bool:
        seen = set()
        s = 0
        while s < 9:
            if board[s][j] in seen:
                return False
            elif board[s][j] != ".":
                seen.add(board[s][j])
            s += 1
        return True