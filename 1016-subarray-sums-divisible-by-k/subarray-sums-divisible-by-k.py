class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prev_cnt = {0:1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum +=num
            mod = (cur_sum % k + k) % k
            if mod in prev_cnt:
                count += prev_cnt[mod]
            prev_cnt[mod] = prev_cnt.get(mod,0)+1
        return count