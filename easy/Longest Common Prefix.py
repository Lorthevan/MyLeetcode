class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        for i in range(len(strs)-1):
            for j in range(len(strs)-i-1):
                if len(strs[j]) > len(strs[j+1]):
                    strs[j], strs[j+1] = strs[j+1], strs[j]
        set_ch = set()
        gen = []
        add = 0
        for i in range(len(strs)):
            gen.append(ch for ch in strs[i])
        for j in range(len(strs[0])):
            for i in range(len(gen)):
                set_ch.add(next(gen[i]))

            else:
                if len(set_ch) == 1:
                    add += 1
                else:
                    break
                set_ch = set()
        return strs[0][:add] if add != 0 else ''