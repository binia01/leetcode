class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        a = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            a[i] = nums[i]

            for j in range(i+1, len(nums)):
                a[j] = max(nums[i]-a[j], nums[j]- a[j-1])
        return a[len(nums)-1] >= 0
        