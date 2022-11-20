class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if(len(intervals) == 0):
            return 0
        intervals.sort(key=lambda x:x[0])
        
        l1 = []
        heapq.heapify(l1)
        heapq.heappush(l1, intervals[0][1])
        for index in range(1, len(intervals)):
            if(l1[0] > intervals[index][0]):
                print(intervals[index])
                heapq.heappush(l1, intervals[index][1])
            else:
                heapq.heappop(l1)
                heapq.heappush(l1, intervals[index][1])
        return len(l1)
            