class Solution:
    def countDistinct(self, s: str) -> int:
        m = {}
        
        def func(st, m):
            # print(st)
            if(len(st) == 0 or st in m):
                return
            elif(len(st) == 1):
                m[st] = True
                return
            
            if(st[1:len(st)] not in m):
                func(st[1:len(st)],m)
            if(st[0:len(st)-1] not in m):
                func(st[0:len(st)-1],m)
            if(st[1:len(st)-1] not in m):
                func(st[1:len(st)-1],m)
            m[st] = True
        
        func(s, m)
#         temp = []
#         for keys in m:
#             # print(keys)
#             temp.append(keys)
        
#         temp.sort()
#         print(temp)
        # print(m, len(m))
        return(len(m)) 