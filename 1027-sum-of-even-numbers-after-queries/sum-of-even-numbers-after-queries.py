class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        init_sum = sum(num for num in nums if num %2 ==0)
        ans = []
        for query in queries:
            val = query[0]
            if nums[query[1]] % 2 == 0:
                init_sum -= nums[query[1]]
                print(init_sum)
            nums[query[1]] += val
            if nums[query[1]] % 2 == 0:
                init_sum += nums[query[1]]
            ans.append(init_sum)   
        return ans  
        
        