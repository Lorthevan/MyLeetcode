class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for s in strs:
            res.setdefault(tuple(sorted(s)), []).append(s)
        return list(res.values())