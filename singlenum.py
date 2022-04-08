class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                dictionary[nums[i]] += 1
            else:
                dictionary[nums[i]] = 1
        for i in dictionary.keys():
            if dictionary[i] == 1:
                return i
