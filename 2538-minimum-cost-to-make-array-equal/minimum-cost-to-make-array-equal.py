class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        res = sorted(zip(nums,cost))
        n = len(nums)//2 
        total = 0
        total_cost = sum(cost)
        pref_cost = 0
        median = None

        for num, cost in res:
            pref_cost += cost
            if pref_cost > total_cost//2:
                median = num 
                break

        for num, cost in res:
            total += ((abs(num - median)) * cost)
            
        return total
            