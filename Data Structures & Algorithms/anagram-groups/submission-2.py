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

        # Better way to write this same code O(m*n logn)
        # res = defaultdict(list)
        # for s in strs:
        #     new_s = ''.join(sorted(s))
        #     res[new_s].append(s)
        # return list(res.values())

        # Another way with O(m*n) considering 26 chars only
        # store the count tuple as key as it's immutable
        # count list only has the count of these alpha
        res = defaultdict(list)
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            res[tuple(count)].append(word)
        return list(res.values())
        
