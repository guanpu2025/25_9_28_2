# encoding: utf-8
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Microsoft YaHei')

SCORE_NONE = -1

class Life(object):
    """个体类"""
    def __init__(self, aGene=None):
        self.gene = aGene
        self.score = SCORE_NONE  # 适配值/得分

random.seed(36)

# 2) 读取城市坐标（文件每行：城市名 \t x \t y）
CITY_FILE = "D:\\xwechat_files\\wxid_ebcbsuw1xvfq22_876a\\msg\\file\\2025-10\\TSP_GA\\TSP_GA\\distanceMatrix.txt"
citys = []
with open(CITY_FILE, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        name, x, y = line.split("\t")
        citys.append((float(x), float(y), name))

# 3) 定义超参数
LIFE_COUNT = 100
CROSS_RATE = 0.6
MUTATION_RATE = 0.03
MAX_GENERATIONS = 2000

# 4) 初始化种群
gene_length = len(citys)
lives = []
base = list(range(gene_length))
for _ in range(LIFE_COUNT):
    g = base[:]
    random.shuffle(g)
    lives.append(Life(g))
    # print(len(g))

# 5) 定义评估函数（回路距离的倒数）
def evaluate(life):
    dist = 0.0
    for i in range(gene_length-1):
        # print(len(life.gene))
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

def select(lives):#轮盘赌
    all_score = 0
    for i in lives:
        all_score += i.score
    if all_score <= 1e-12:
        return random.choice(lives)
    r = random.uniform(0, all_score)
    for i in lives:
        r -= i.score
        if r <= 0:
            return i
    return random.choice(lives)

def fork(father, mother):
    if random.random() > CROSS_RATE:
        return father.gene.copy()
    
    start = random.randint(0, gene_length - 1)
    end = random.randint(start + 1, gene_length)

    son = [None] * gene_length
    son[start:end] = father.gene[start:end]

    mom_num = end % gene_length

    for i in range(end, end + gene_length):
        cur = i % gene_length
        if cur in range(start, end):
            continue
        while mother.gene[mom_num]  in father.gene[start:end]:
            mom_num += 1
            mom_num %= gene_length
        son[cur] = mother.gene[mom_num]
        mom_num += 1
        mom_num %= gene_length
    
    return son

def tubian(g):
    g_2 = g.copy()
    if random.random() < MUTATION_RATE:  
        i = random.randint(0, gene_length - 2)
        j = random.randint(i + 1, gene_length - 1)
        g_2[i:j+1] = g_2[i:j+1][::-1]
    return g_2

# 6) GA 主循环
best_history = []
best = None

for gen in range(MAX_GENERATIONS):
    for i in lives:
        if i.score == SCORE_NONE:
            i.score = evaluate(i)
    cur_best = max(lives, key=lambda x: x.score)
    if(best == None) or (cur_best.score > best.score):
        best = Life(cur_best.gene.copy())
        best.score = cur_best.score
    best_history.append(1.0 / best.score)

    new_lives = []
    new_lives.append(Life(cur_best.gene.copy()))

    while len(new_lives) < LIFE_COUNT:
        mother = select(lives)
        father = select(lives)
        son = fork(mother, father)
        son = tubian(son)
        new_lives.append(Life(son))

    lives = new_lives
    for j in lives:
        j.score = SCORE_NONE

# 7) 输出结果
final_best_distance = 1.0 / best.score
print(f"经过 {MAX_GENERATIONS} 次迭代，最优解距离为：{final_best_distance:.6f}")
print("遍历城市顺序为：")
for idx in best.gene:
    print(citys[idx][2], end=' -> ')
print(citys[best.gene[0]][2])

# 8) 可视化
best_cycle = best.gene[:] + [best.gene[0]]

plt.figure(figsize=(6, 10))
# 历史最优曲线
plt.subplot(2, 1, 1)
plt.plot(best_history, 'r-', label='history_best')
plt.xlabel('Iteration')
plt.ylabel('length')
plt.legend()

# 最优路线
plt.subplot(2, 1, 2)
xs = [citys[i][0] for i in best_cycle]
ys = [citys[i][1] for i in best_cycle]
plt.plot(xs, ys, 'g-')
plt.plot(xs, ys, 'r.')
for (x, y, name) in citys:
    plt.text(x * 1.001, y * 1.001, name, fontsize=8)
plt.xlabel('x')
plt.ylabel('y')

plt.tight_layout()
plt.savefig('final.png', dpi=500)
plt.show()
plt.close()