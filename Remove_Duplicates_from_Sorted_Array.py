class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        len_nums = len(nums)
        if len_nums == 0:
            return 0
        n = 0
        for i in range(1, len_nums):
            if nums[i] == nums[i-1]:
                continue
            else:
                n+=1
                nums[n] = nums[i]
        return n+1
s = Solution()
print(s.removeDuplicates([1, 1, 2]))