class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans=1
        start=0
        mask=0

        for end in range(len(nums)):
            while mask&nums[end]:
                mask^=nums[start]
                start+=1
            mask|=nums[end]
            ans=max(ans,end-start+1)
        return ans
