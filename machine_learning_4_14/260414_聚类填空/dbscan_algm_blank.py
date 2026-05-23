import numpy as np
import seaborn as sns
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from collections import deque


def minkowski_distance(x, y=0, p=2):
    return np.linalg.norm(x - y, ord=p)


def find_neighbors(x, dataset, eps, p=2): 
    """
    在 dataset 中寻找样本 x 的 eps-邻域 N_eps(x)

    参数:
        x: 当前样本
        dataset: 数据集
        eps: 邻域半径
        p: 闵可夫斯基距离参数

    返回:
        邻居样本下标列表
    """
    neis = []
    for i, sample in enumerate(dataset):
        # TODO: 计算距离
        dist = minkowski_distance(x, sample, p)
        if dist <= eps:  # TODO: 判断条件
            neis.append(i)
    return neis


def dbscan(dataset, eps, min_pts, p=2, seed=0):
    """
    DBSCAN 实现

    输入:
        dataset: 样本集 D
        eps: 邻域参数 eps
        min_pts: 邻域内至少包含 min_pts 个样本则视为核心对象
        p: 闵可夫斯基距离参数
        seed: 随机种子, 用于“随机选取一个核心对象”

    返回:
        C: 长度为 n 的列表, C[i] 表示第 i 个样本所属的类簇编号
           其中 0 表示噪声点
        k: 最终生成的聚类簇个数
    """
    rng = np.random.default_rng(seed)
    n = len(dataset)
    neighbors = []                  # 保存每个样本的 eps-邻域
    omega = set()                   # 核心对象集合 Ω, 用样本下标表示
    for j in range(n):
        neis = find_neighbors(dataset[j], dataset, eps, p)
        neighbors.append(neis)
        if len(neis) >= min_pts:
            omega.add(j)
    k = 0                           # 初始化聚类簇数 k = 0
    Gamma = set(range(n))           # 初始化未访问样本集合 Γ = D
    C = [0 for _ in range(n)]       # 初始化最终类别向量
    while len(omega) > 0:           # while Ω != ∅ do
        Gamma_old = Gamma.copy()    #   Γ_old = Γ
        o = rng.choice(list(omega)) #   随机选取一个核心对象 o ∈ Ω
        Q = deque([o])              #   初始化队列 Q = <o>
        if o in Gamma:
            Gamma.remove(o)         #   Γ = Γ \ {o}
        while len(Q) > 0:           #   while Q != ∅ do
            q = Q.popleft()
            if len(neighbors[q]) >= min_pts:              #       TODO: 判断条件
                Delta = set(neighbors[q]) & Gamma
                for sample_idx in Delta:
                    Q.append(sample_idx)            #       TODO: 扩展待访问队列
                Gamma = Gamma - Delta
        k += 1                      # k = k + 1
        Ck = Gamma_old - Gamma      # 生成聚类簇 C_k = Γ_old \ Γ
        for idx in Ck:
            C[idx] = k
        omega = omega - Ck          # Ω = Ω \ C_k
    return C, k


def draw(dataset, C, m):
    """
    按类别绘制聚类结果
    C[i] = 0 的样本视为噪声点, 用 x 标记
    """
    current_palette = sns.color_palette()
    sns.set_theme(context="talk", palette=current_palette)

    clus = [[] for _ in range(m + 1)]
    for i, clu_idx in enumerate(C):
        clus[clu_idx].append(dataset[i])

    # 绘制各个聚类簇
    for clu in clus[1:]:
        xs, ys = [], []
        for sample in clu:
            xs.append(sample[0])
            ys.append(sample[1])
        sns.scatterplot(x=xs, y=ys)

    # 绘制噪声点
    xs, ys = [], []
    for sample in clus[0]:
        xs.append(sample[0])
        ys.append(sample[1])
    if len(xs) > 0:
        sns.scatterplot(x=xs, y=ys, marker='x')

    plt.show()


if __name__ == '__main__':
    dataset = np.loadtxt("./watermelon.txt")
    eps = 0.11
    min_pts = 5
    p = 2
    seed = 9

    C, m = dbscan(dataset, eps, min_pts, p, seed)
    draw(dataset, C, m)