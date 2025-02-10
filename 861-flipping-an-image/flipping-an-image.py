class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        grid = []
        for i in range(len(image)):
            grid.append(image[i][::-1])
        for i in range(len(image)):
            for j in range(len(image[0])):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                elif grid[i][j] == 1:
                    grid[i][j] = 0
        return grid