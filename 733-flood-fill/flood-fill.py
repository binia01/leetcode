class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original_color = image[sr][sc]
        if original_color == color:
            return image

        def func(row, col):
            if (row < 0 or row >= len(image) or
                col < 0 or col >= len(image[0]) or
                image[row][col] != original_color):
                return
            image[row][col] = color
            func(row+1, col)
            func(row-1, col)
            func(row, col+1)
            func(row, col-1)

        func(sr, sc)
        return image
