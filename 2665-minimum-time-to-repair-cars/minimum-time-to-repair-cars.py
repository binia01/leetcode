class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(time):
            count = 0
            for rank in ranks:
                count += int(sqrt(time/rank))
            return count
        low, high = 1, ranks[0] * (cars ** 2)
        ans = 0

        while low <= high:
            mid = (low+ high)//2
            rep = check(mid)

            if rep >= cars:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

        
            

        