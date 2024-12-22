class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        cur_height = 1
        count =[0]*101

        for height in heights:
            count[height] +=1
        for height in heights:
            while count[cur_height] ==0:
                cur_height +=1
            if height != cur_height:
                ans+=1
            count[cur_height]-=1

        return ans
        