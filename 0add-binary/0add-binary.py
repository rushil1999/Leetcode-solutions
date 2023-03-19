class Solution:
    def addBinary(self, a: str, b: str) -> str:
        padding = ""
        for i in range(max(len(a), len(b)) - min(len(a), len(b)) ):
            padding+= "0"
        if(len(a) > len(b)):
            b = padding + b
        elif(len(a)<len(b)):
            a = padding + a
        
        val = ""
        carry = "0"
        print(a,b)
        for i in range(len(a)-1, -1, -1):
            if((a[i] == "1" and b[i] =="0") or (a[i] == "0" and b[i] =="1")):
                if(carry == "0"):
                    val = "1" + val
                else:
                    val = "0"+val
            elif(a[i] =="0" and b[i] =="0"):
                if(carry == "0" ):
                    val = "0"+val
                else:
                    val = "1" + val
                    carry = "0"
            else:
                if(carry == "0" ):
                    val = "0"+val
                    carry = "1"
                else:
                    val = "1" + val
            print(val)
        print(val)
        if(carry == "1"):
            val = carry + val
        return val