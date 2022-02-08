class Solution:
    def isValid(self, s: str) -> bool:
        array = ['()', '{}', '[]']
        for i in array:
            if i in s:
                return self.isValid(s.replace(i, ''))
        if s == '':
            return True
        return False























