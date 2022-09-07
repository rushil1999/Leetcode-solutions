class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        meetingList = [intervals[0][1]]
        heapq.heapify(meetingList)
        for index in range(1, len(intervals)):
            top = heapq.heappop(meetingList)
            if(intervals[index][0] < top):
                heapq.heappush(meetingList, intervals[index][1])
                heapq.heappush(meetingList, top)
            else:
                heapq.heappush(meetingList, intervals[index][1])
        print(meetingList)
        return len(meetingList)