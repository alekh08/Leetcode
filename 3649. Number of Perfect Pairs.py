class Solution:
    def perfectPairs(self, nums: List[int]) -> int:

        arr = sorted(abs(x) for x in nums)
        n = len(arr)
        res = 0
        r = 0
        
        for l in range(n):
            if r < l + 1:
                r = l + 1
            while r < n and arr[r] <= 2 * arr[l]:
                r += 1
            res += r - l - 1
        
        return res
            
