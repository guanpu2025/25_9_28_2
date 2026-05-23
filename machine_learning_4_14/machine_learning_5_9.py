from sklearn.datasets import make_blobs
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import StandardScaler, LabelEncoder
import copy
from sklearn.model_selection import train_test_split

def generate_2d_data(n_samples=1000, centers=2, random_state=42, class_sep=1.0):
    X, y = make_blobs(n_samples=n_samples, n_features=2, centers=centers,
                      cluster_std=1.0, center_box=(-5, 5),
                      random_state=random_state)
    y = np.where(y == 0, -1, 1)
    return X.astype(np.float32), y.astype(np.int8)

X_rand, y_rand = generate_2d_data(1000, centers=2, random_state=42)
print(X_rand.shape, y_rand.shape)

plt.figure(figsize=(6,5))
plt.scatter(X_rand[y_rand==1][:,0], X_rand[y_rand==1][:,1],
            c='deepskyblue', edgecolor='k', label='Class +1')
plt.scatter(X_rand[y_rand==-1][:,0], X_rand[y_rand==-1][:,1],
            c='salmon', edgecolor='k', label='Class -1')
plt.legend()
plt.title("Random 2D Dataset (1000 samples)")
plt.xlabel("Feature 1"); plt.ylabel("Feature 2")
plt.show()


def load_heart_disease():
    # 加载数据集
    heart = fetch_openml(data_id=1455, as_frame=True, parser='pandas')
    X = heart.data.copy()
    y = heart.target.copy()

    # --- 1. 处理目标值 y（转换为 +1/-1）---
    unique_y = y.unique()
    print("原始目标标签:", unique_y)
    if 'no' in unique_y and 'yes' in unique_y:
        y = y.map({'no': -1, 'yes': 1})
    elif 'absent' in unique_y and 'present' in unique_y:
        y = y.map({'absent': -1, 'present': 1})
    else:
        le = LabelEncoder()
        y = le.fit_transform(y)
        y = np.where(y == 0, -1, 1)
    y = y.astype(np.int8)

    # --- 2. 处理特征 X（将非数值列编码为数值）---
    # 检查每一列的数据类型
    for col in X.columns:
        if X[col].dtype == 'object' or X[col].dtype.name == 'category':
            # 对分类列进行 LabelEncoder
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))
        # 如果已经是数值类型，保持不变

    # 确认所有列都是数值类型
    X = X.astype(float)   # 确保浮点数

    # 标准化
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y

X_real, y_real = load_heart_disease()
print(f"数据集维度: {X_real.shape}, 正例: {np.sum(y_real==1)}, 负例: {np.sum(y_real==-1)}")

# ===================== 核函数 =====================
class Kernel:
    @staticmethod
    def linear(x1, x2):
        return np.dot(x1, x2)

    @staticmethod
    def rbf(x1, x2, gamma=0.5):
        diff = x1 - x2
        return np.exp(-gamma * np.dot(diff, diff))

# ===================== SMO 算法 =====================
class SMO:
    def __init__(self, C=1.0, tol=0.001, max_passes=20, kernel='linear', gamma=0.5):
        self.C = C
        self.tol = tol
        self.max_passes = max_passes
        self.kernel_type = kernel
        self.gamma = gamma
        self.alphas = None
        self.b = 0.0
        self.X = None
        self.y = None
        self.K = None          # Gram 矩阵
        self.n = 0
        self.eps = 1e-8

    def _kernel_func(self, x1, x2):
        if self.kernel_type == 'linear':
            return Kernel.linear(x1, x2)
        else:   # rbf
            return Kernel.rbf(x1, x2, self.gamma)

    def _compute_gram(self, X):
        n = X.shape[0]
        K = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                K[i, j] = self._kernel_func(X[i], X[j])
        return K

    def _f_x(self, i):
        # 决策函数输出 f(x_i)
        total = self.b
        for j in range(self.n):
            if self.alphas[j] > 0:
                total += self.alphas[j] * self.y[j] * self.K[j, i]
        return total

    def _E(self, i):
        return self._f_x(i) - self.y[i]
    
    
    def _take_step(self, i1, i2):
        if i1 == i2:
            return False
        alph1 = self.alphas[i1]
        alph2 = self.alphas[i2]
        y1 = self.y[i1]
        y2 = self.y[i2]
        E1 = self._E(i1)
        E2 = self._E(i2)
        s = y1 * y2

        # 计算 alpha2 的边界
        if y1 != y2:
            L = max(0, alph2 - alph1)
            H = min(self.C, self.C + alph2 - alph1)
        else:
            L = max(0, alph1 + alph2 - self.C)
            H = min(self.C, alph1 + alph2)
        if abs(L - H) < self.eps:
            return False

        k11 = self.K[i1, i1]
        k12 = self.K[i1, i2]
        k22 = self.K[i2, i2]
        eta = k11 + k22 - 2 * k12
        if eta > 0:
            a2_new = alph2 + y2 * (E1 - E2) / eta
            if a2_new < L:
                a2_new = L
            elif a2_new > H:
                a2_new = H
        else:
            # 特殊情况，沿边界遍历
            f1 = y1 * (E1 + self.b) - alph1 * k11 - s * alph2 * k12
            f2 = y2 * (E2 + self.b) - s * alph1 * k12 - alph2 * k22
            L1 = alph1 + s * (alph2 - L)
            H1 = alph1 + s * (alph2 - H)
            objL = L1 * f1 + L * f2 + 0.5 * (L1**2 * k11 + L**2 * k22 + 2 * s * L1 * L * k12)
            objH = H1 * f1 + H * f2 + 0.5 * (H1**2 * k11 + H**2 * k22 + 2 * s * H1 * H * k12)
            if objL < objH - self.eps:
                a2_new = L
            elif objL > objH + self.eps:
                a2_new = H
            else:
                a2_new = alph2
        if abs(a2_new - alph2) < self.eps * (a2_new + alph2 + self.eps):
            return False
        a1_new = alph1 + s * (alph2 - a2_new)
        if a1_new < 0:
            a1_new = 0
        elif a1_new > self.C:
            a1_new = self.C

        # 更新 b
        b1 = -E1 - y1 * (a1_new - alph1) * k11 - y2 * (a2_new - alph2) * k12 + self.b
        b2 = -E2 - y1 * (a1_new - alph1) * k12 - y2 * (a2_new - alph2) * k22 + self.b
        if 0 < a1_new < self.C:
            self.b = b1
        elif 0 < a2_new < self.C:
            self.b = b2
        else:
            self.b = (b1 + b2) / 2

        # 更新 alpha
        self.alphas[i1] = a1_new
        self.alphas[i2] = a2_new
        return True

    def fit(self, X, y):
        self.X = X
        self.y = y
        self.n = X.shape[0]
        self.alphas = np.zeros(self.n)
        self.b = 0.0
        self.K = self._compute_gram(X)

        passes = 0
        while passes < self.max_passes:
            num_changed = 0
            for i in range(self.n):
                Ei = self._E(i)
                ri = Ei * self.y[i]
                # KKT 违反判断
                if (ri < -self.tol and self.alphas[i] < self.C) or (ri > self.tol and self.alphas[i] > 0):
                    # 选择第二个变量 j (简单循环，也可采用最大步长)
                    j = np.random.choice([idx for idx in range(self.n) if idx != i])
                    if self._take_step(i, j):
                        num_changed += 1
            if num_changed == 0:
                passes += 1
            else:
                passes = 0

        # 存储支持向量
        self.sv_idx = np.where(self.alphas > self.eps)[0]
        self.sv_X = self.X[self.sv_idx]
        self.sv_y = self.y[self.sv_idx]
        self.sv_alphas = self.alphas[self.sv_idx]

    def predict(self, X_new):
        y_pred = []
        for x in X_new:
            f = self.b
            for i in range(len(self.sv_idx)):
                f += self.sv_alphas[i] * self.sv_y[i] * self._kernel_func(self.sv_X[i], x)
            y_pred.append(np.sign(f))
        return np.array(y_pred)
    
def to_numpy_y(y):
        """确保 y 是 1D numpy 数组且值为 int8"""
        if hasattr(y, 'values'):
            y = y.values
        y = np.asarray(y).ravel().astype(np.int8)
        return y

    
def check_all_kkt(model, X, y, C, tol=0.001):
    """检查所有训练样本是否满足 KKT 条件，返回值: (violations, max_r, min_r)"""
    violations = 0
    r_list = []
    n = X.shape[0]
    for i in range(n):
        # 计算 f(x_i)
        f = model.b
        for j in range(len(model.sv_idx)):
            f += model.sv_alphas[j] * model.sv_y[j] * model._kernel_func(model.sv_X[j], X[i])
        Ei = f - y[i]
        ri = Ei * y[i]
        r_list.append(ri)
        if (ri < -tol and model.alphas[i] < C) or (ri > tol and model.alphas[i] > 0):
            violations += 1
    print(f"KKT 违反数: {violations}/{n} (max_r={max(r_list):.6f}, min_r={min(r_list):.6f})")
    if violations == 0:
        print("所有样本满足 KKT 条件 (gold standard satisfied!)")
    else:
        print("仍存在 KKT 违反样本")
    return violations, max(r_list), min(r_list)

def plot_2d_boundary_margin(model, X, y, title, ax=None):
    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 6))
    # 网格范围
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    grid = np.c_[xx.ravel(), yy.ravel()]
    # 预测决策值
    Z = []
    for point in grid:
        f = model.b
        for i in range(len(model.sv_idx)):
            f += model.sv_alphas[i] * model.sv_y[i] * model._kernel_func(model.sv_X[i], point)
        Z.append(f)
    Z = np.array(Z).reshape(xx.shape)

    # 绘制决策面 (0) 和间隔线 (±1)
    ax.contour(xx, yy, Z, levels=[-1, 0, 1],
               linestyles=['--', '-', '--'],
               colors=['#4d4d4d', 'black', '#4d4d4d'],
               linewidths=1.5)
    # 绘制数据点
    ax.scatter(X[y==1][:,0], X[y==1][:,1], c='deepskyblue', edgecolor='k', label='+1')
    ax.scatter(X[y==-1][:,0], X[y==-1][:,1], c='salmon', edgecolor='k', label='-1')
    # 绘制支持向量
    sv = model.sv_X
    ax.scatter(sv[:,0], sv[:,1], s=100, facecolors='none', edgecolors='k', linewidths=1.5,
               label='Support Vectors')
    ax.set_title(title)
    ax.legend()
    return ax

print("\n========== 实验 1：随机 1000 个二维样本 ==========")

# 取前 200 个样本（可改为全部 1000，但训练稍慢）
X_train, _, y_train, _ = train_test_split(X_rand, y_rand, train_size=200, random_state=42)
y_train = to_numpy_y(y_train)   # 确保为 numpy 数组

for kernel_name in ['linear', 'rbf']:
    print(f"\n--- 核: {kernel_name} ---")
    model = SMO(C=1.0, tol=0.001, max_passes=20, kernel=kernel_name, gamma=0.5)
    model.fit(X_train, y_train)
    check_all_kkt(model, X_train, y_train, C=1.0, tol=0.001)
    fig, ax = plt.subplots(figsize=(8,6))
    plot_2d_boundary_margin(model, X_train, y_train,
                            title=f"Random Dataset ({kernel_name} kernel)", ax=ax)
    plt.show()

print("\n========== 实验 2：真实数据集 Heart Disease (前两个特征) ==========")
X_real_2d = X_real[:, :2]
Xr_train, Xr_test, yr_train, yr_test = train_test_split(X_real_2d, y_real, train_size=0.8, random_state=42)
yr_train = to_numpy_y(yr_train)
yr_test = to_numpy_y(yr_test)

for kernel_name in ['linear', 'rbf']:
    print(f"\n--- 核: {kernel_name} ---")
    model_real = SMO(C=1.0, tol=0.001, max_passes=20, kernel=kernel_name, gamma=0.5)
    model_real.fit(Xr_train, yr_train)
    check_all_kkt(model_real, Xr_train, yr_train, C=1.0, tol=0.001)
    y_pred = model_real.predict(Xr_test)
    acc = np.mean(y_pred == yr_test)
    print(f"测试准确率: {acc*100:.2f}%") 
    fig, ax = plt.subplots(figsize=(8,6))
    plot_2d_boundary_margin(model_real, Xr_train, yr_train,
                            title=f"Heart Disease ({kernel_name} kernel, 2 features)", ax=ax)
    plt.show()

print("\n========== 附加验证：真实数据集全特征 (不画二维图) ==========")
Xr_full_train, _, yr_full_train, _ = train_test_split(X_real, y_real, train_size=0.8, random_state=42)
yr_full_train = to_numpy_y(yr_full_train)

for kernel_name in ['linear', 'rbf']:
    print(f"\n--- 全特征，核: {kernel_name} ---")
    model_full = SMO(C=1.0, tol=0.001, max_passes=20, kernel=kernel_name, gamma=0.5)
    model_full.fit(Xr_full_train, yr_full_train)
    check_all_kkt(model_full, Xr_full_train, yr_full_train, C=1.0, tol=0.001)