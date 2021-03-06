class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxnum = nums[0]
        now = nums[0]
        for i in range(1, len(nums)):
            now = max(nums[i], now + nums[i])
            maxnum = max(now, maxnum)
        return maxnum
