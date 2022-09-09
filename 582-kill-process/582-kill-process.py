class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        parentChildMap = {}
        root = 0
        
        for index in range(0,len(ppid)):
            parent = ppid[index]
            child = pid[index]
            if(parent == 0):
                root = child
                print("Root", root)
                continue            
            if(parent not in parentChildMap):
                parentChildMap[parent] = [child]
            else:
                parentChildMap[parent].append(child)
        
        print(parentChildMap)
        
        
        
        if(kill == root):
            stack = [(root, True)]
        else:
            stack = [(root, False)]
        print("Stack Initialized", stack)
        killed = []
        
        while(len(stack )> 0):
            top = stack[0]
            stack = stack[1:len(stack)]
            print(top[0])
            if(top[1] == False and top[0] != kill):
                killFlag = False
            else:
                killed.append(top[0])
                killFlag = True
            if(top[0] in parentChildMap):
                for child in parentChildMap[top[0]]:
                    stack.append((child, killFlag))
        
        return killed
                
            
        