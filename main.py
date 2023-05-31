from city import *
from ant import *
import random

LOOPS = 100 # số lần lặp
n = 3 # số lần chạy bài toán
nbOfCity = 20 # số lượng thành phố
nbOfAnt = 10 # số lượng kiến
P = 0.5 # hệ số bay hơi [0, 1]
Q = 1 # hệ số cường độ pheromone
bestDistance = 0 # Khoảng cách tôi ưu ban đầu
bestPath = [] # Mảng chứa đường đi tối ưu nhất

# Khởi tạo ma trận khoảng cách giữa các thành phố và mùi
tp = City()
tp.city =  [[0 if i == j else random.randint(1, 10) for j in range(nbOfCity)] for i in range(nbOfCity)]
tp.pheromone = [[1 if i != j else 0 for j in range(nbOfCity)] for i in range(nbOfCity)]
# In thành phố random vừa tạo
print("Thành phố vừa tạo")
for i in tp.city:
    print(i)
# tao dan kien 10 con
ants = [Ant(nbOfCity) for _ in range(nbOfAnt)]


print(f"Chu trình hamilton ngắn nhất của {n} lần test")
# lặp n lần để test kết quả
for _ in range(n):
    # vòng lặp chính của thuật toán
    for loop in range(LOOPS):
        # Thả đàn kiếm tìm đường
        for ant in ants: 
            # Tạo điểm xuất phát ngẫu nhiên cho con kiến
            start = random.randint(0, nbOfCity-1)
            ant.path.append(start)
            ant.visited[start] = True
            
            # Lựa chọn đường đi của con kiến dựa trên xác xuất
            while len(ant.path) < nbOfCity: 
                for i in range(nbOfCity):
                    rd = random.random()
                    if ant.visited[i] == False and rd <= tp.Probabilities(ant.GetLastCity(), i):
                        ant.path.append(i)
                        ant.visited[i] = True
            # Thêm điểm ban đầu để hoàn thành chu trình
            ant.path.append(start)
            
            # Cập nhật lại khoảng cách con kiến vừa tìm được
            ant.totalDistance = ant.DistanceTraveled(tp.city)
            if loop == 0:
                bestDistance = ant.totalDistance
                bestPath = ant.path
            elif bestDistance > ant.totalDistance:
                bestDistance = ant.totalDistance
                bestPath = ant.path
                
        #cập nhật lại ma trận mùi (pheromone) do đàn kiến vừa tạo và reset
        for ant in ants:
            for i in range(len(ant.path)-1):
                begin = ant.path[i]
                end = ant.path[i+1]
                tp.pheromone[begin][end] *= 1 - P
                tp.pheromone[begin][end] += Q/ant.totalDistance
            ant.Reset()
    #in kết quả của lần test thứ n
    print(bestPath, end="\t")
    print(f"Tổng đường đi: {bestDistance}")