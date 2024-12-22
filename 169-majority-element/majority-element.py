class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_num = {}
        for num in nums:
            count_num[num] = count_num.get(num,0)+1
        most_freq = max(count_num, key= count_num.get)
        return most_freq


        