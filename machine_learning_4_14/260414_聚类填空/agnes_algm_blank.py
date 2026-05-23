import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


def minkowski_distance(x, y, p=2):
    return np.linalg.norm(x - y, ord=p)

def d_ave(c_i, c_j, p=2):
    """平均距离 / 均链接"""
    sum_dist = 0.0
    for x in c_i:
        for y in c_j:
            sum_dist += minkowski_distance(x, y, p)
    ave_dist = sum_dist / (len(c_i) * len(c_j))    # TODO: 计算平均距离
    return ave_dist

def d_min(c_i, c_j, p=2):
    """最小距离 / 单链接"""
    min_dist = np.inf
    for x in c_i:
        for y in c_j:
            min_dist = min(min_dist, minkowski_distance(x, y, p))
    return min_dist


def d_max(c_i, c_j, p=2):
    """最大距离 / 全链接"""
    max_dist = 0.0
    for x in c_i:
        for y in c_j:
            max_dist = max(max_dist, minkowski_distance(x, y, p))
    return max_dist


def find_min(M):
    """
    在距离矩阵 M 中找出距离最近的两个聚类簇
    返回: i*, j*, min_dist
    """
    min_dist = np.inf
    i_star, j_star = -1, -1
    q = len(M)

    for i in range(q):
        for j in range(i + 1, q):
            if M[i][j] < min_dist:
                min_dist = M[i][j]
                i_star, j_star = i, j    # TODO: 更新当前最小距离及其对应的两个簇下标

    return i_star, j_star, min_dist


def AGNES(dataset, dist_func, k, p=2):
    """
    AGNES 代码实现
    :param dataset: 数据集
    :param dist_func: 簇间距离函数 d_min / d_max / d_ave
    :param k: 目标类簇个数
    :param p: 闵可夫斯基距离参数
    :return: 聚类结果 C
    """
    dataset = np.asarray(dataset)
    m = len(dataset)

    if k < 1 or k > m:
        raise ValueError("k 必须满足 1 <= k <= m")

    C = []                          # 当前聚类簇集合 C = [C1, C2, ..., Cq]
    for j in range(m):              # for j = 1, 2, ..., m do
        C.append([dataset[j]])      #   C_j = {x_j}
    M = []                          # 距离矩阵 M
    for i in range(m):              # for i = 1, 2, ..., m do
        M_i = []
        for j in range(m):          #   for j = 1, 2, ..., m do
            dist = dist_func(C[i], C[j], p) # M(i, j) = d(C_i, C_j)
            M_i.append(dist)
        M.append(M_i)
    q = m                           # q = m
    while q > k:                    # while q > k do
        i_star, j_star, min_dist = find_min(M)  # 找出距离最近的两个聚类簇 C_i* 和 C_j*
        C[i_star].extend(C[j_star]) # TODO: C_i* = C_i* ∪ C_j*
        C.pop(j_star)               # C_j 重编号为 C_{j-1}
        M.pop(j_star)               # 删除距离矩阵 M 的第 j* 行与第 j* 列
        for row in M:
            row.pop(j_star)
        for j in range(q - 1):      # for j = 1, 2, ..., q - 1 do
            if j != i_star:
                new_dist = dist_func(C[i_star], C[j], p)
                M[i_star][j] = new_dist
                M[j][i_star] = new_dist                    # TODO: 更新簇间距离
        q = q - 1                   # q = q - 1
    
    return C                        # 输出: 簇划分 C = {C1, C2, ..., Ck}


def draw(C, title="AGNES Clustering Result"):
    sns.set_theme(style="whitegrid", context="talk", rc={"font.family": "Consolas"})
    palette = sns.color_palette("tab10", n_colors=len(C))

    plt.figure(figsize=(8, 6))
    for i, clu in enumerate(C):
        clu = np.asarray(clu)
        plt.scatter(
            clu[:, 0],
            clu[:, 1],
            s=80,
            color=palette[i],
            label=f"Cluster {i + 1}"
        )

    plt.title(title)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    p = 2
    k = 3
    dataset = np.loadtxt("./watermelon.txt")

    C = AGNES(dataset, dist_func=d_ave, k=k, p=p)

    print("聚类结果：")
    for i, clu in enumerate(C, 1):
        print(f"簇 {i}:") 
        for sample in clu:
            print(sample)

    draw(C, title="d_ave; k=3")