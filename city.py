class City:
    def __init__(self) -> None:
        self.city = [] # ma trận khoảng cách các thành phố
        self.pheromone = [] # ma trận mùi
        self.alpha = 1
        self.beta = 1
        self.P = 0.5 # hệ số bay hơi
        self.Q = 1 # hệ số cường độ pheromone
        
    # trả về khoảng cách giữa i và j
    def GetDistance(self, i : int, j : int) -> float:
        return self.city[i][j]
    
    # trả về mùi giữa i và j
    def GetPher(self, i : int, j : int) -> float:
        return self.pheromone[i][j]
    
    # trả về xác xuất con kiến đi từ i tới j trong khoảng 0 -> 1
    def Probabilities(self, i : int, j : int) -> float:
        if i == j:
            return 0
        m = 0 
        for l in range(len(self.city)):
            if l == i:
                continue
            m += self.GetPher(i, l)**self.alpha * (1/self.GetDistance(i, l))**self.beta
        return (self.GetPher(i, j)**self.alpha * (1/self.GetDistance(i, j))**self.beta) / m
    
    # Cập nhật lại pheromore từ đường đi của con kiến
    def UpdatePheromone(self, ant) -> None:
        for i in range(len(ant.path)-1):
            begin = ant.path[i]
            end = ant.path[i+1]
            self.pheromone[begin][end] *= 1 - self.P
            self.pheromone[begin][end] += self.Q/ant.totalDistance
    