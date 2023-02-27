class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [100001 for _ in range(n+1)]
        graph = {}
        for time in times:
            source = time[0]
            destination = time[1]
            t = time[2]
            if(source in graph):
                graph[source].append((destination, t))
            else:
                graph[source] = [(destination, t)]
        dp[k] = 0 
        queue = [k]
        while(len(queue)>0):
            top = queue[0]
            queue = queue[1:len(queue)]
            if(top in graph):
                for destination in graph[top]:
                    if(dp[destination[0]] > destination[1]+dp[top]):
                        dp[destination[0]] = dp[top]+destination[1]
                        queue.append(destination[0])
        minimumValue = 0
        for i in range(1,n+1):
            if(dp[i] == 100001):
                return -1
            minimumValue = max(dp[i], minimumValue)
        return minimumValue

