from city import *
from ant import *
import random

n = 5 # số lần test bài toán
nbOfCity = 10 # số lượng thành phố      
nbOfAnt = 30 # số lượng kiến
LOOPS = 30 # số lần lặp thuật toán
bestDistance = 0 # Khoảng cách tôi ưu ban đầu
bestPath = [] # Mảng chứa đường đi tối ưu nhất

# Khởi tạo ma trận khoảng cách giữa các thành phố
tp = City()
tp.city =  [[0 for _ in range(nbOfCity)] for _ in range(nbOfCity)]
for i in range(nbOfCity):
    for j in range(nbOfCity):
        if i != j:
            if j > i:
                tp.city[i][j] = random.randint(1, 30)
            else:
                tp.city[i][j] = tp.city[j][i]

# In thành phố random vừa tạo
print("Thành phố vừa tạo")
for i in tp.city:
    print(i)
# Tạo đàn kiến
ants = [Ant() for _ in range(nbOfAnt)]

print(f"Chu trình hamilton ngắn nhất của {n} lần test")
# lặp n lần để test kết quả
for _ in range(n):
    # Khởi tạo lại ma trận pheromone sau mỗi lần test
    tp.pheromone = [[1 if i != j else 0 for j in range(nbOfCity)] for i in range(nbOfCity)]
    # vòng lặp chính của thuật toán
    for loop in range(LOOPS):
        # Thả đàn kiếm tìm đường
        for ant in ants: 
            # Tạo điểm xuất phát ngẫu nhiên cho con kiến
            start = random.randint(0, nbOfCity-1)
            ant.path.append(start)
            # Lựa chọn đường đi của con kiến dựa trên xác xuất
            while len(ant.path) < nbOfCity: 
                for i in range(nbOfCity):
                    rd = random.random()
                    if i not in ant.path and rd <= tp.Probabilities(ant.LastCity(), i):
                        ant.path.append(i)
            # Thêm điểm ban đầu để hoàn thành chu trình
            ant.path.append(start)
            ant.totalDistance = ant.DistanceTraveled(tp.city)

        for ant in ants:
            #cập nhật lại ma trận mùi (pheromone) do đàn kiến vừa tạo
            tp.UpdatePheromone(ant)
            # Cập nhật lại khoảng cách con kiến vừa tìm được
            if loop == 0:
                bestDistance = ant.totalDistance
                bestPath = ant.path
            elif bestDistance > ant.totalDistance:
                bestDistance = ant.totalDistance
                bestPath = ant.path
            #Reset lại đàn kiến và đi tới lần lặp tiếp theo
            ant.Reset()
    #in kết quả của lần test thứ n
    print(bestPath, end="\t")
    print(f"Tổng đường đi: {bestDistance}")