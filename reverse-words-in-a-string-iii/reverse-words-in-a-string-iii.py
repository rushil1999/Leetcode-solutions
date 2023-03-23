class Solution:
    def reverseWords(self, st: str) -> str:
        i = 0
        s = []
        for i in range(len(st)):
            s.append(st[i])
        # print('before',s)
        i = 0
        while(i<len(s)):
            if(s[i] != ' '):
                start = i
                j = i
                while(j<len(s) and s[j] != ' '):
                    j+= 1
                
                end = j-1
                # print("Caught", start, end, s[start], s[end])
                
                mid = (start+end)//2
                for k in range(start, mid+1):
                    temp = s[k]
                    s[k] = s[start + (end-k)]
                    s[start+ (end-k)] = temp
                # print(s[start:end+1])
                i = j
            else:
                i+= 1
        return "".join(s)