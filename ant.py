class Ant:   
    def __init__(self) -> None:
        self.path = [] # mảng đường đi của kiến
        self.totalDistance = 0 # Tổng khoảng cách con kiến đã đi dc
        
    #trả về thành phố cuối cùng con kiến đi qua
    def LastCity(self) -> int:
        return self.path[-1]
    
    # trả vê tổng khoảng cách con kiến đã đi qua
    def DistanceTraveled(self, DistanceMatrix : list) -> float:
        t = 0 
        for i in range(len(self.path)-1):
            start = self.path[i]
            end = self.path[i+1]
            t += DistanceMatrix[start][end]
        return t
    
    # Reset lại con kiến
    def Reset(self) -> None:
        self.path = []
        self.totalDistance = 0