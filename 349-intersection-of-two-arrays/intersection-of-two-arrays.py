class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        s = set()
        l = r = 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r]:
                s.add(nums1[l])
                l+=1
                r+=1
            elif nums1[l] < nums2[r]:
                l+=1
            else:
                r+=1
        return list(s)
        
            


            