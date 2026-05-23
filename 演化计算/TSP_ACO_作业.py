import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Microsoft YaHei')

#random.seed(40240202)

city_file = "D:\\xwechat_files\\wxid_ebcbsuw1xvfq22_876a\\msg\\file\\2025-10\\TSP_GA\\TSP_GA\\distanceMatrix.txt"
city = []

def calculate(x1, y1, x2, y2):
    return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

with open(city_file, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.split("\t")
        if len(parts) == 3:
            city.append((parts[0], float(parts[1]), float(parts[2])))
n = len(city)
dist_juzhen = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        if(i == j):
            dist_juzhen[i][j] = float('inf')
        else:
            x1, y1 = city[i][1], city[i][2]
            x2, y2 = city[j][1], city[j][2]
            dist_juzhen[i][j] = calculate(x1, y1, x2, y2)

m = 40                    #蚂蚁数量
alpha = 1.0
beta = 2.0
zhengfa = 0.2
Q = 100

information = np.ones((n, n)) * 0.5

def select(cur_city, city):
    all_score = 0
    for i in city:
        qifa = 1.0 / dist_juzhen[cur_city][i]
        all_score += (information[cur_city][i] ** alpha) * (qifa ** beta)
    if(all_score <= 1e-12):
        return random.choice(city)
    r = random.uniform(0, all_score)
    for i in city:
        qifa = 1.0 / dist_juzhen[cur_city][i]
        r -= (information[cur_city][i] ** alpha) * (qifa ** beta)
        if r <= 0:
            return i
    return random.choice(city)

def build_path():
    n = len(city)
    start = random.randint(0, n - 1)
    vis = set([start])
    path = [start]
    path_len = 0.0
    cur = start
    while len(vis) < n:
        next = [j for j in range(n) if j not in vis]
        temp = select(cur, next)
        vis.add(temp)
        path.append(temp)
        path_len += dist_juzhen[cur, temp]
        cur = temp 

    path.append(start)
    path_len += dist_juzhen[start, cur]
    return path, path_len

def renew(all_path, all_length):
    for i in range(n):
        for j in range(i, n):
            information[i][j] = (1 - zhengfa) * information[i][j]
            information[j][i] = (1 - zhengfa) * information[j][i]
    for k in range(m):
        path = all_path[k]
        length = all_length[k]
        for i in range(len(path) - 1):
            city_i = path[i]
            city_j = path[i + 1]
            information[city_i][city_j] += Q / length * alpha
            information[city_j][city_i] += Q / length * alpha

global_best_path = None
global_min_len = float('inf')
max_time = 200
best_history = []
best_path = None
min_len = float('inf')

for i in range(max_time):
    all_paths = []
    all_len = []
    for j in range(m):
        cur_path, cur_len = build_path()
        all_paths.append(cur_path)
        all_len.append(cur_len)
        if cur_len < min_len:
            min_len = cur_len
            best_path = cur_path
    if global_min_len > min_len:
        global_min_len = min_len
        global_best_path = best_path
    best_history.append(global_min_len)
    
    renew(all_paths, all_len)

print(f"经{max_time}次迭代后，最优解为{global_min_len:.6f}")
for i in range(n):
    city_name = city[global_best_path[i]][0]
    if i == len(global_best_path) - 1:
        print(city_name)
    else:
        print(f"{city_name}->", end="")

plt.figure(figsize=(6, 10))
plt.subplot(2, 1, 1)
plt.plot(best_history, 'r-', label='history_best')
plt.xlabel('Iteration')
plt.ylabel('length')
plt.legend()

plt.subplot(2, 1, 2)
xs = [city[i][1] for i in global_best_path]
ys = [city[i][2] for i in global_best_path]
plt.plot(xs, ys, 'g-')
plt.plot(xs, ys, 'r.')
for (name, x, y) in city:
    plt.text(x * 1.001, y * 1.001, name, fontsize=8)
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
#plt.savefig('final.png', dpi=500)
plt.show()
plt.close()