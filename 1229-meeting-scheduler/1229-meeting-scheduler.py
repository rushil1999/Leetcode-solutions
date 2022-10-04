class Solution:
        
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        ptr1 = ptr2 = 0
        while(ptr1 < len(slots1) and ptr2 < len(slots2)):
            if(slots1[ptr1][1] >= slots2[ptr2][0] and slots1[ptr1][1] <= slots2[ptr2][1]):
                startingVal = max(slots1[ptr1][0], slots2[ptr2][0])
                d = slots1[ptr1][1] - startingVal
                if(d >=duration):
                    print("H 1")
                    return [startingVal, startingVal+duration]
                ptr1 += 1
            elif(slots1[ptr1][1] <= slots2[ptr2][0]):
                ptr1 += 1
            elif(slots2[ptr2][1] >= slots1[ptr1][0] and slots2[ptr2][1] <= slots1[ptr1][1]):
                startingVal = max(slots1[ptr1][0], slots2[ptr2][0])
                d = slots2[ptr2][1] - startingVal
                if(d >=duration):
                    print("H 2", d, slots2[ptr2][1], slots1[ptr1][0])
                    return [startingVal, startingVal+duration]
                ptr2 += 1
            else:
                ptr2 += 1
        return [] 
            
            
            
            
            # if(slots1[ptr1][0] < slots[ptr2][0]):
            #     d = self.overlapDuration(slots1[ptr1][0], slots1[ptr][1], slots2[ptr][0], slots2[ptr][0])
            #     if(d >= duration ):
            #         return [slots1[ptr1], slots1[ptr1]+d]
            # if(slots2[ptr1][0] < slot1[ptr2][0]):
            #     d = self.overlapDuration(slots1[ptr1][0], slots1[ptr][1], slots2[ptr][0], slots2[ptr][0])
            #     if(d >= duration ):
            #         return [slots2[ptr2], slots2[ptr2]+d]
            