from city import *
from ant import *
from fileTest import *
import random

LOOPS = 100 # số lần lặp
P = 0.5 # hệ số bay hơi [0, 1]
Q = 1 # hệ số cường độ pheromone
bestDistance = 100 # Khoảng cách tôi ưu ban đầu
bestPath = [] # Mảng chứa đường đi tối ưu nhất

# Khởi tạo ma trận khoảng cách giữa các thành phố và mùi
tp = City()
tp.city =  matrix4x4_1
tp.pheromore = pher4x4

# tao dan kien 10 con
ants = [Ant(len(tp.city)) for _ in range(10)]

# Lặp lại nhiều lần
for _ in range(LOOPS):
    # Thả đàn kiếm tìm đường
    for ant in ants: 
        # Tạo điểm xuất phát ngẫu nhiên cho con kiến
        start = random.randint(0, len(tp.city)-1)
        ant.path.append(start)
        ant.visited[start] = True
        
        # Lựa chọn đường đi của con kiến dựa trên xác xuất
        while len(ant.path) < len(tp.city): 
            for i in range(len(tp.city)):
                rd = random.random()
                if ant.visited[i] == False and rd <= tp.Probabilities(ant.GetLastCity(), i):
                    ant.path.append(i)
                    ant.visited[i] = True
        
        # Cập nhật lại khoảng cách con kiến vừa tìm được
        ant.totalDistance = ant.GetDistanceTraveled(tp.city)
        if bestDistance > ant.totalDistance:
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

print(bestPath)