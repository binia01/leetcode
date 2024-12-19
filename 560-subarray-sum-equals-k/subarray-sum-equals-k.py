class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_cnt = {0:1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum +=num
            if cur_sum - k in prev_cnt:
                count += prev_cnt[cur_sum - k]
            prev_cnt[cur_sum] = prev_cnt.get(cur_sum,0)+1
        return count
        