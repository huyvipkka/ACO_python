class City:
    
    def __init__(self) -> None:
        self.city = [] # ma trận khoảng cách các thành phố
        self.pheromone = [] # ma trận mùi
        self.alpha = 1
        self.beta = 1
        
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
    