class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        height_diffs_heap = []
      
        for i in range(len(heights) - 1):
            current_height = heights[i]
            next_height = heights[i + 1]
            height_diff = next_height - current_height
            if height_diff > 0:
                heappush(height_diffs_heap, height_diff)
                if len(height_diffs_heap) > ladders:
                    bricks -= heappop(height_diffs_heap)
                    if bricks < 0:
                        return i

        return len(heights) - 1