class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n=len(nums)
        a=[]
        b=(1<<maximumBit)-1
        for i in nums:
            a.append(b^i)
            b=b^i
        a.reverse()
        return a
