class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num,0)+1
        
        max_num = -1
        max_count = 0

        for num, counts in count.items():
            if counts > max_count:
                max_num = num
                max_count = counts
            elif counts == max_count:
                max_num = min(max_num,num)
        return max_num
            

        
        