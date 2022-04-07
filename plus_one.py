class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for i in digits:
            s += str(i)
        s = str((int(s) + 1))
        res = []
        for i in s:
            res.append(int(i))
        return res

