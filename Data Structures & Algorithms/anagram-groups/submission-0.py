from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        res = []
        for s in strs:
            new_s = ''.join(sorted(s))
            if new_s in d:
                d[new_s].append(s)
            else:
                d[new_s]=[s]

        for v in d.values():
            res.append(v)
        return res