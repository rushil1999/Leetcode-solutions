class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        sm = {}
        tm = {}
        f = ""
        for index in range(0, len(indices)):
            sm[indices[index]] = sources[index]
            tm[indices[index]] = targets[index]
        
        index = 0
        while(index < len(s)):
            
            print("Index", index)
            if(index not in sm):
                f += s[index]
                index += 1
                continue
            str = s[index:index+len(sm[index])]
            print(str)
            if(str == sm[index]):
                f += tm[index]
                index = index + len(sm[index])
            else:
                f += s[index]
                index += 1
        return f