class Solution:
  def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    row = len(mat)
    col = len(mat[0])
    queue = deque()
    seen = [[0] * col for _ in range(row)]

    for i in range(row):
      for j in range(col):
        if mat[i][j] == 0:
          queue.append((i, j))
          seen[i][j] = 1


    while queue:
      i, j = queue.popleft()
      for dx, dy in directions:
        x = i + dx
        y = j + dy
        if (x >= 0 and x < row) and (y >= 0 and y < col) and seen[x][y] == 0:
            mat[x][y] = mat[i][j] + 1
            queue.append((x, y))
            seen[x][y] = True

    return mat