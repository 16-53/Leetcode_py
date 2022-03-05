class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i



