class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        print(points)
        count = 1
        cur_st = points[0][0]
        cur_end = points[0][1]
        for st, end in points[1:]:
            if st <= cur_end:
                cur_end = min(end, cur_end)
            else:
                count+=1
                cur_st = st
                cur_end = end
                
        return count

        