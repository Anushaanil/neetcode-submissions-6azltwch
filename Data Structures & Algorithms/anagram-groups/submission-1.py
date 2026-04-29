from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # OG
        # d = {}
        # res = []
        # for s in strs:
        #     new_s = ''.join(sorted(s))
        #     if new_s in d:
        #         d[new_s].append(s)
        #     else:
        #         d[new_s]=[s]

        # for v in d.values():
        #     res.append(v)
        # return res

        # Better way to write this same code
        res = defaultdict(list)
        for s in strs:
            new_s = ''.join(sorted(s))
            res[new_s].append(s)
        return list(res.values())
