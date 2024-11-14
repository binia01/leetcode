class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        start,end = 0, n-1
        max_area = 0
        while start < end:
            width = n - start - (n - end)
            con_height = height[end] if height[end] <= height[start] else height[start]
            cur_area = width * con_height
            if cur_area > max_area:
                max_area = cur_area
            if height[end] > height[start]:
                start += 1
            else:
                end -= 1
        return max_area        
        