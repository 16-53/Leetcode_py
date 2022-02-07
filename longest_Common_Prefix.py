class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        len_strs = len(strs)
        
        if len_strs == 1:
            return strs[0]
        
        strs.sort(key = lambda s: len(s))
        first_word = strs[0]
        repeats = []
        
        for i in range(1, len_strs):
            s = ''
            n = 0
            while n <= len(first_word) - 1:
                if first_word[n] == strs[i][n]:
                    s += first_word[n]
                else:
                    n = len(first_word)
                n += 1
            repeats.append(s)
        repeats.sort(key = lambda s: len(s))
        return repeats[0]
