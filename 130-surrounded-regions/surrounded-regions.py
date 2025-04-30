class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(i,j):
            board[i][j] = "."
            directions = [[0,1],[0,-1],[1,0],[-1,0]]

            for dire in directions:
                x = i + dire[0]
                y = j + dire[1]
                if 0 <= x < row and 0 <= y < col and board[x][y] == "O":
                    dfs(x,y)

        row, col = len(board), len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i == 0 or i == row-1 or j == 0 or j == col - 1 ):
                    dfs(i,j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == ".":
                    board[i][j] = "O"
