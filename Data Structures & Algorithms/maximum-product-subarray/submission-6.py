class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmax, curmin = 1, 1

        for n in nums:
            tmp = n*curmax
            curmax = max(tmp, curmin*n, n)
            curmin = min(tmp, n*curmin, n)
            res = max(res, curmax)
        return res