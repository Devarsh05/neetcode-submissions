class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curmin, curmax = 1, 1 

        for n in nums:
            tmp = n *curmax
            curmax = max(n*curmax, n, n*curmin)
            curmin = min(tmp, n, n*curmin)
            res = max(res, curmax)
        return res