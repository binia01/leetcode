class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        result = [-1, -1]

        while start <= end:
            mid = (start + (end - start)//2)

            if nums[mid] == target:
                result[0] = mid
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + (end - start)//2)

            if nums[mid] == target:
                result[1] = mid
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return result
        