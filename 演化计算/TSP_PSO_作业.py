import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font', family='Microsoft YaHei')

#random.seed(36)

class Particle:#每条旅行路径  
    def __init__(self, gene=None):
        self.gene = gene
        self.best_gene = gene.copy() if gene else None
        self.fitness = -1
        self.best_fitness = -1
        self.velocity = []

class PSO_TSP:
    def __init__(self, citys, pop_size=100, max_iter=3000, w_start=0.9, w_end=0.4, c1=1.4, c2=1.4):
        self.citys = citys  # (x, y, name)
        self.num_cities = len(citys)
        self.pop_size = pop_size
        self.max_iter = max_iter
        self.w_start = w_start
        self.w_end = w_end
        self.c1 = c1
        self.c2 = c2

        self.global_best_gene = None
        self.global_best_fitness = -1
        self.particles = []
        self.best_history = []
        self.diversity_history = []
        
        self.init_particles()
    
    def init_particles(self):
        base = list(range(self.num_cities))
        for _ in range(self.pop_size):
            if random.random() < 0.3:
                gene = self._neighbor_initialization()
            else:
                gene = base.copy()
                random.shuffle(gene)
            particle = Particle(gene)
            self.evaluate(particle)
            self.particles.append(particle)
            
            if particle.fitness > self.global_best_fitness:
                self.global_best_fitness = particle.fitness
                self.global_best_gene = gene.copy()
    
    def _neighbor_initialization(self):
        gene = []
        visited = set()
        current = random.randint(0, self.num_cities - 1)#随便选一个起点
        gene.append(current)
        visited.add(current)
        
        while len(gene) < self.num_cities:
            min_dist = float('inf')
            next_city = -1
            x1, y1, _ = self.citys[current]
            for city in range(self.num_cities):
                if city not in visited:
                    x2, y2, _ = self.citys[city]
                    dist = math.hypot(x1 - x2, y1 - y2)
                    if dist < min_dist:
                        min_dist = dist
                        next_city = city
            gene.append(next_city)
            visited.add(next_city)
            current = next_city
        return gene
    
    def evaluate(self, particle):
        dist = 0.0
        gene = particle.gene
        for i in range(self.num_cities - 1):
            i1 = gene[i]
            i2 = gene[i + 1]
            x1, y1, _ = self.citys[i1]
            x2, y2, _ = self.citys[i2]
            dist += math.hypot(x1 - x2, y1 - y2)
        
        last = gene[-1]
        first = gene[0]
        x1, y1, _ = self.citys[last]
        x2, y2, _ = self.citys[first]
        dist += math.hypot(x1 - x2, y1 - y2)
        
        particle.fitness = 1.0 / max(1e-12, dist)
    
    def get_velocity(self, particle, current_iter):
        w = self.w_start - (self.w_start - self.w_end) * (current_iter / self.max_iter)
        
        velocity = []
        diff_pbest = self.calculate_difference(particle.gene.copy(), particle.best_gene)
        diff_gbest = self.calculate_difference(particle.gene.copy(), self.global_best_gene)
        
        for swap in diff_pbest:
            if random.random() < self.c1 / (self.c1 + self.c2) and swap not in velocity:
                velocity.append(swap)
        
        for swap in diff_gbest:
            if random.random() < self.c2 / (self.c1 + self.c2) and swap not in velocity:
                velocity.append(swap)
        
        for swap in particle.velocity:
            if random.random() < w and swap not in velocity:
                velocity.append(swap)
        
        max_velocity_length = max(2, int(self.num_cities * 0.1))#最多交换10%
        if len(velocity) > max_velocity_length:
            velocity = random.sample(velocity, max_velocity_length)
        
        return velocity
    
    def calculate_difference(self, gene1, gene2):
        diff = []
        pos = {city: idx for idx, city in enumerate(gene1)}
        
        for i in range(self.num_cities):
            if gene1[i] != gene2[i]:
                j = pos[gene2[i]]
                if i < j:
                    diff.append((i, j))
                else:
                    diff.append((j, i))
                gene1[i], gene1[j] = gene1[j], gene1[i]
                pos[gene1[i]] = i
                pos[gene1[j]] = j
        
        return diff
    
    def update_position(self, particle):
        new_gene = particle.gene.copy()
        shuffled_velocity = random.sample(particle.velocity, len(particle.velocity))
        for i, j in shuffled_velocity:
            if i != j and 0 <= i < self.num_cities and 0 <= j < self.num_cities:
                new_gene[i], new_gene[j] = new_gene[j], new_gene[i]
        return new_gene
    
    def mutate(self, gene, rate=0.1):
        if random.random() < rate:
            if random.random() < 0.5:
                i = random.randint(0, self.num_cities - 2)
                j = random.randint(i + 1, self.num_cities - 1)
                gene[i:j+1] = gene[i:j+1][::-1]
            else:
                i = random.randint(0, self.num_cities - 1)
                j = random.randint(0, self.num_cities - 1)
                if i != j:
                    gene[i], gene[j] = gene[j], gene[i]
        return gene
    
    def _evaluate_diversity(self):
        if len(self.particles) < 2:
            return 0.0
        total_diff = 0
        for p in self.particles:
            diff = self.calculate_difference(p.gene.copy(), self.global_best_gene)
            total_diff += len(diff)
        return total_diff / len(self.particles)
    
    def is_converged(self, gen):
        if gen < 200:
            return False
        distance_change = self.best_history[gen-200] - self.best_history[gen]
        diversity = self.diversity_history[gen]
        return distance_change <= 3.0 and diversity < self.num_cities * 0.2
    
    def run(self):
        for gen in range(self.max_iter):
            #精英保留
            elite_gene = self.global_best_gene.copy()
            elite_fitness = self.global_best_fitness
            
            for particle in self.particles:#更新
                particle.velocity = self.get_velocity(particle, gen)
                new_gene = self.update_position(particle)
                new_gene = self.mutate(new_gene)
                particle.gene = new_gene

                self.evaluate(particle)
                
                if particle.fitness > particle.best_fitness:
                    particle.best_fitness = particle.fitness
                    particle.best_gene = new_gene.copy()
                
                if particle.fitness > self.global_best_fitness:
                    self.global_best_fitness = particle.fitness
                    self.global_best_gene = new_gene.copy()
            
            if self.global_best_fitness < elite_fitness:
                self.global_best_gene = elite_gene
                self.global_best_fitness = elite_fitness
                random.choice(self.particles).gene = elite_gene.copy()
            
            if gen % 50 == 0 and gen > 0:#全局最优变异
                mutated_gene = self.global_best_gene.copy()
                self.mutate(mutated_gene, rate=0.3)
                temp_particle = Particle(mutated_gene)
                self.evaluate(temp_particle)
                if temp_particle.fitness > self.global_best_fitness:
                    self.global_best_gene = mutated_gene
                    self.global_best_fitness = temp_particle.fitness
            
            self.best_history.append(1.0 / self.global_best_fitness)
            self.diversity_history.append(self._evaluate_diversity())
            if gen % 200 == 0:  # 每200代打印一次
                print(f"第{gen}代，当前最优距离：{self.best_history[-1]:.6f}公里，种群多样性：{self.diversity_history[-1]:.1f}")            
            if gen > 0 and self.is_converged(gen):
                print(f"在第{gen}代收敛")
                break
        
        return self.global_best_gene, self.best_history, gen

if __name__ == "__main__":
    CITY_FILE = "D:\\xwechat_files\\wxid_ebcbsuw1xvfq22_876a\\msg\\file\\2025-10\\TSP_GA\\TSP_GA\\distanceMatrix.txt"
    citys = []
    with open(CITY_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t") 
            if len(parts) == 3:    
                name, x, y = parts
                citys.append((float(x), float(y), name))
    
    
    pso = PSO_TSP(citys, pop_size=100, max_iter=3001, w_start=0.9, w_end=0.4, c1=1.4,  c2=1.4)
    best_gene, best_history, gen = pso.run()
    
    final_best_distance = 1.0 / pso.global_best_fitness
    print(f"\n经过{gen}次迭代，最优路径总距离：{final_best_distance:.6f}公里")
    print("最优遍历顺序：")
    for i, idx in enumerate(best_gene):
        print(citys[idx][2], end=' -> ')
    print(citys[best_gene[0]][2])
    
    best_cycle = best_gene[:] + [best_gene[0]]
    plt.figure(figsize=(8, 12))
    
    plt.subplot(2, 1, 1)
    plt.plot(best_history, 'r-', linewidth=1.5, label='每代最优距离')
    plt.xlabel('迭代次数', fontsize=10)
    plt.ylabel('路径总长度（公里）', fontsize=10)
    plt.title('PSO求解TSP：最优距离优化曲线', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.subplot(2, 1, 2)
    xs = [citys[i][0] for i in best_cycle]
    ys = [citys[i][1] for i in best_cycle]
    plt.plot(xs, ys, 'g-', alpha=0.8, linewidth=1.2, label='最优路径')
    plt.scatter(xs, ys, c='r', s=60, alpha=0.9, label='城市')

    for (x, y, name) in citys:
        plt.text(x, y, name, fontsize=8, ha='center', va='bottom')
    plt.xlabel('经度', fontsize=10)
    plt.ylabel('纬度', fontsize=10)
    plt.title('最优旅行路径', fontsize=12)
    plt.legend()   
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()