class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                if cur_sum == target:
                    return target
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                if cur_sum < target:
                    l +=1
                else:
                    r-=1
        return closest
        