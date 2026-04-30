class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        res = ""
        for s in strs:
            # form new string with len and $
            res += str(len(s)) + "$" + s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
            
        res_list = []
        start, end = 0, len(s)
    
        while start < end:
            # cur keeps track of length value till $
            cur = start
            while s[cur] != "$":
                cur+=1
            length = int(s[start:cur])
            
            # fetch ele after $ before length of chars
            res_list.append(str(s[cur + 1 : cur + 1 + length]))
            
            # re initialize start with new ele
            start = cur + 1 + length
            
        return res_list
