from city import *
from ant import *
from fileTest import *
import random

LOOPS = 100 # so lan lap
P = 0.5 # hệ số bay hơi [0, 1]
Q = 1 # hệ số cường độ pheromone
bestDistance = 100 # khoang cach toi uu ban dau
bestPath = [] #mang chua vet toi uu nhat

# khoi tao ma tran cac thanh pho
tp = City()
tp.city =  matrix4x4_1
tp.pheromore = pher4x4

# tao dan kien 10 con
ants = [Ant(len(tp.city)) for _ in range(10)]

for _ in range(LOOPS): # lap lai nhieu lan
    # Thả đàn kiếm cho kiến tìm đường
    for ant in ants: 
        # moi con kien bat dau tai 1 noi ngau nhien
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
        
        # cap nhap khoang cach moi theo duong di con kien vua tim dc
        ant.totalDistance = ant.GetDistanceTraveled(tp.city)
        if bestDistance > ant.totalDistance:
            bestDistance = ant.totalDistance
            bestPath = ant.path
            
    #cập nhật lại ma trận mùi (pheromore) do đàn kiến vừa tạo và reset
    for ant in ants:
        for i in range(len(ant.path)-1):
            begin = ant.path[i]
            end = ant.path[i+1]
            tp.pheromore[begin][end] *= 1 - P
            tp.pheromore[begin][end] += Q/ant.totalDistance
        ant.Reset()

print(bestPath)