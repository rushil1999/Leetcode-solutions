class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        final = [[intervals[0][0], intervals[0][1]]]
        current = [intervals[0][0], intervals[0][1]]
        for index in range(1, len(intervals)):
            if(final[-1][1] >= intervals[index][0]):
                current = final[-1]
                final = final[0:len(final)-1]
                final.append([current[0], max(intervals[index][1], current[1])] )
            else:
                final.append([intervals[index][0], intervals[index][1]])
 
        return final