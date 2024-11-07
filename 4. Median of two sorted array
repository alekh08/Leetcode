class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=[]
        i=j=0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        merged.extend(nums1[i:])
        merged.extend(nums2[j:])
        total = len(merged)
        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            mid1 = merged[total // 2 - 1]
            mid2 = merged[total // 2]
            return (mid1 + mid2) / 2.0
