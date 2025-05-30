class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result_xor = 0
        if len(nums2) % 2:
            for num in nums1:
                result_xor ^= num
        if len(nums1) % 2:
            for num in nums2:
                result_xor ^= num
        return result_xor