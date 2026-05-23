import random
import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.rc('font', family='Microsoft YaHei')

#random.seed(36)

CITY_FILE = "D:\\xwechat_files\\wxid_ebcbsuw1xvfq22_876a\\msg\\file\\2025-10\\TSP_GA\\TSP_GA\\distanceMatrix.txt"
citys = []
with open(CITY_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, x, y = line.split("\t")
        citys.append((float(x), float(y), name))

gene_length = len(citys)

class Life(object):
    def __init__(self, aGene=None):
        self.gene = aGene
        self.score = -1
        self.best_score = -1
        self.v = []

def evaluate(life):
    dist = 0.0
    for i in range(gene_length-1):
        i1 = life.gene[i]
        i2 = life.gene[i + 1]
        x1, y1, _ = citys[i1]
        x2, y2, _ = citys[i2]
        dist += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    last_city = life.gene[-1]
    first_city = life.gene[0]
    x1, y1, _ = citys[last_city]
    x2, y2, _ = citys[first_city]
    dist += math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return 1.0 / max(1e-12, dist)

F = 0.8
CR = 0.9
NP = 80                                  #种群数
best_score = float("-inf")
best_history = None
max_generation = 1000
best_distances = []

lives = []
base = list(range(gene_length))
for _ in range(NP):
    g = base[:]
    random.shuffle(g)
    G = Life(g)
    G.score = evaluate(G)
    lives.append(G)

def tubian(g0):
    g_temp = g0.copy()
    i = random.randint(0, gene_length - 2)
    j = random.randint(i + 1, gene_length - 1)
    g_temp[i], g_temp[j] = g_temp[j], g_temp[i]
    return g_temp

def pmx_crossover(parent_gene, mutant_gene, cr):
    trail = parent_gene.copy()
    if random.random() <= cr:
        i, j = sorted(random.sample(range(gene_length), 2))
        mutant_seg = mutant_gene[i:j+1]
        parent_seg = trail[i:j+1]
        trail[i:j+1] = mutant_seg
        for k in range(gene_length):
            if i <= k <= j:
                continue
            if trail[k] in mutant_seg:
                idx = mutant_seg.index(trail[k])
                trail[k] = parent_seg[idx]
    return trail

for i in range(max_generation):
    for j in range(NP - 1):
        r0 = random.randint(0, NP - 1)
        r1 = random.randint(0, NP - 1)
        r2 = random.randint(0, NP - 1)

        while r0 == r1:
            r1 = random.randint(0, NP - 1)
        while r0 == r2:
            r2 = random.randint(0, NP - 1)

        mutant = tubian(lives[r0].gene)

        trail_gene = pmx_crossover(lives[r0].gene, mutant, CR)
        trail = Life(trail_gene)
        trail.score = evaluate(trail)

        if trail.score > lives[j].score:
            lives[j] = trail

    current_best = max(lives, key=lambda x: x.score)
    current_best_distance = 1 / current_best.score
    best_distances.append(current_best_distance)
    
    if current_best.score > best_score:
        best_score = current_best.score
        best_history = current_best.gene.copy()

print(1 / best_score)
plt.figure(figsize=(6, 10))
# 历史最优曲线
plt.subplot(2, 1, 1)
plt.plot(best_distances, 'r-', label='history_best')
plt.xlabel('Iteration')
plt.ylabel('length')
plt.legend()

# 最优路线
plt.subplot(2, 1, 2)
xs = [citys[i][0] for i in best_history]
ys = [citys[i][1] for i in best_history]
xs.append(xs[0])
ys.append(ys[0])
plt.plot(xs, ys, 'g-')
plt.plot(xs, ys, 'r.')
for (x, y, name) in citys:
    plt.text(x * 1.001, y * 1.001, name, fontsize=8)
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.show()
plt.close()