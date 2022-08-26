class UndergroundSystem:

    def __init__(self):
        self.roundTrips = {}
        self.checkInMap = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
        return None

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkInMap[id][0]
        checkInTime = self.checkInMap[id][1]
        if((startStation, stationName) not in self.roundTrips):
            self.roundTrips[(startStation, stationName)] = [t - checkInTime]
        else:
            self.roundTrips[(startStation, stationName)].append(t-checkInTime)
        return None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime = 0
        for tripTime in self.roundTrips[(startStation, endStation)]:
            totalTime += tripTime
        return totalTime/len(self.roundTrips[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)