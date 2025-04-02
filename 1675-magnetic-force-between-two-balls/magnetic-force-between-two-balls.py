class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(name):
            prev = position[0]
            count = 1

            for pos in position[1:]:
                if pos - prev >= name:
                    prev = pos
                    count +=1
            return count 
        
        position.sort()
        left, right = 1, position[-1] - position[0]

        while left < right:
            mid = (left + right+1) // 2

            if check(mid) >= m:
                left = mid
            else:
                right = mid - 1
        return left
        