import numpy as np


class SMOSVM:
    def __init__(self, C=1.0, kernel="linear", gamma=None, tol=1e-3, max_iter=10000, eps_alpha=1e-12, random_state=None):
        #C是惩罚系数，选择线性核（还有什么核？），gamma是RBF核参数，越大决策边界越复杂
        #tol是KKT容忍误差，用于判断是否已经收敛，max_iter最大迭代次数
        #eps_alpha判断 alpha 是否为 0 的数值阈值。因为浮点数不可能完全精确。
        self.C = float(C)
        self.kernel = kernel.lower()
        self.gamma = gamma
        self.tol = float(tol)
        self.max_iter = int(max_iter)
        self.eps_alpha = float(eps_alpha)
        self.random_state = random_state
        self.alpha_ = None
        self.b_ = 0.0
        self.support_vectors_ = None
        self.support_labels_ = None
        self.support_alpha_ = None
        self.support_indices_ = None
        self._X_train = None
        self._y_train = None
        self._K = None
        self.kkt_history_ = []

    def gramjuzhen(self, X):#gram矩阵，所有样本之间的核函数值
        if self.kernel == "linear":
            return X @ X.T
        if self.kernel == "rbf":
            g = self.gamma if self.gamma is not None else 1.0 / X.shape[1]
            sq = np.sum(X * X, axis=1)
            d2 = sq[:, None] + sq[None, :] - 2.0 * (X @ X.T)
            d2 = np.maximum(d2, 0.0)
            return np.exp(-g * d2)
        raise ValueError("unknown kernel")

    def decision(self, k_row):#决策函数
        return float(np.dot(self.alpha_ * self._y_train, k_row) + self.b_)

    def decision_function(self, X):#给出决策值
        if self.kernel == "linear":
            w = np.sum((self.alpha_ * self._y_train)[:, None] * self._X_train, axis=0)
            return X @ w + self.b_
        g = self.gamma if self.gamma is not None else 1.0 / self._X_train.shape[1]
        t = self._X_train
        sq_t = np.sum(t * t, axis=1)
        sq_x = np.sum(X * X, axis=1)[:, None]#完全向量化，快
        d2 = sq_x + sq_t - 2.0 * (X @ t.T)
        d2 = np.maximum(d2, 0.0)
        Kq = np.exp(-g * d2)
        return (Kq @ (self.alpha_ * self._y_train)) + self.b_

    def predict(self, X):#从决策值给出类别
        return np.sign(self.decision_function(X))

    def take_step(self, i, j, y, alpha, E):#更新alpha，y是训练标签，E是误差缓存Ei​=f(xi​)−yi​
        if i == j:
            return False
        K = self._K#核矩阵
        alpha_i_old, alpha_j_old = alpha[i], alpha[j]
        yi, yj = y[i], y[j]
        if yi != yj:
            L = max(0.0, alpha_j_old - alpha_i_old)#yj的最小值
            H = min(self.C, self.C + alpha_j_old - alpha_i_old)
        else:
            L = max(0.0, alpha_i_old + alpha_j_old - self.C)
            H = min(self.C, alpha_i_old + alpha_j_old)
        if L >= H - 1e-12:#区间不合法或者实在太小了
            return False
        eta = K[i, i] + K[j, j] - 2.0 * K[i, j]#曲率
        if eta <= 1e-12:
            return False
        Ej, Ei = E[j], E[i]
        alpha_j_new = alpha_j_old + yj * (Ei - Ej) / eta
        alpha_j_new = min(H, max(L, alpha_j_new))
        if abs(alpha_j_new - alpha_j_old) < 1e-12:
            return False
        alpha_i_new = alpha_i_old + yi * yj * (alpha_j_old - alpha_j_new)
        b_old = self.b_
        b1 = -Ei - yi * (alpha_i_new - alpha_i_old) * K[i, i] - yj * (alpha_j_new - alpha_j_old) * K[i, j] + b_old
        b2 = -Ej - yi * (alpha_i_new - alpha_i_old) * K[i, j] - yj * (alpha_j_new - alpha_j_old) * K[j, j] + b_old
        if 0 < alpha_i_new < self.C:
            self.b_ = b1
        elif 0 < alpha_j_new < self.C:
            self.b_ = b2
        else:
            self.b_ = 0.5 * (b1 + b2)#哪个可靠用哪个算，否则取平均值
        alpha[i], alpha[j] = alpha_i_new, alpha_j_new
        #for t in (i, j):
        #    E[t] = self._decision_from_kernel_row(K[:, t]) - y[t]
        for t in range(len(y)):
            E[t] = self.decision(K[:, t]) - y[t]
        return True

    '''def _select_j(self, m, i, E, rng):
        Ei = E[i]
        idx = [j for j in range(m) if j != i]
        best_j = idx[int(np.argmax(np.abs(E[idx] - Ei)))]
        if rng.random() < 0.15:#15%的概率随便选，否则可能老纠结几个点
            best_j = int(rng.choice(idx))
        return best_j'''
    def select_j(self, m, i, E, alpha, rng):
        Ei = E[i]
        #优先从非边界选择
        non_bound_idx = np.where((alpha > self.eps_alpha) & (alpha < self.C - self.eps_alpha))[0]
        non_bound_idx = non_bound_idx[non_bound_idx != i]
        
        if len(non_bound_idx) > 0:
            best_j = non_bound_idx[np.argmax(np.abs(E[non_bound_idx] - Ei))]
        else:
            idx = np.arange(m)
            idx = idx[idx != i]
            best_j = rng.choice(idx)
        if rng.random() < 0.15:
            idx = np.arange(m)
            idx = idx[idx != i]
            best_j = rng.choice(idx)
        
        return best_j

    def fit(self, X, y):
        X = np.asarray(X, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64).ravel()
        if not np.all(np.isin(y, [-1.0, 1.0])):
            raise ValueError("labels must be -1 or +1")
        rng = np.random.default_rng(self.random_state)
        m = X.shape[0]
        self._X_train = X.copy()
        self._y_train = y.copy()
        self._K = self.gramjuzhen(X)#提前缓存会快一点
        alpha = np.zeros(m)
        self.alpha_ = alpha
        self.b_ = 0.0
        self.kkt_history_ = []
        E = np.array([self.decision(self._K[:, k]) - y[k] for k in range(m)])
        examine_all = True
        it = 0
        while it < self.max_iter:
            num_changed = 0
            if examine_all:
                indices = list(range(m))
            else:
                indices = [t for t in range(m) if 0 < alpha[t] < self.C]
                if not indices:
                    indices = list(range(m))
            for i in indices:
                Ei = E[i]
                ri = y[i] * Ei
                #判断有没有违反KKT
                cond_viol = (ri < -self.tol and alpha[i] < self.C - self.eps_alpha) or (ri > self.tol and alpha[i] > self.eps_alpha)
                if not cond_viol:
                    continue
                j = self.select_j(m, i, E, alpha, rng)
                if self.take_step(i, j, y, alpha, E):
                    num_changed += 1
            it += 1
            max_v, _ = self.kkt(alpha, y, E.copy())
            if max_v <= self.tol and num_changed == 0:
                break
            self.kkt_history_.append(max_v)
            if num_changed == 0:
                examine_all = not examine_all
            else:
                examine_all = False
        self.alpha_ = alpha
        self.support_vectors()
        self.max_kkt_violation_, self.mean_abs_dual_eq_ = self.kkt(self.alpha_, y, E)
        self.n_iterations_ = it
        return self

    def kkt(self, alpha, y, E):#计算当前解离KKT最优条件还有多远
        m = len(y)
        viol = []
        for i in range(m):
            ai = alpha[i]
            r = y[i] * E[i]
            if ai < self.eps_alpha:
                v = max(0.0, -r)
            elif ai > self.C - self.eps_alpha:
                v = max(0.0, r)
            else:
                v = abs(r)
            viol.append(v)
        dual_eq = float(np.abs(np.dot(alpha, y)))
        return float(np.max(viol)), dual_eq

    def kkt_violations_per_sample(self):#样本自己的违反程度
        m = len(self._y_train)
        E = np.array([self.decision(self._K[:, k]) - self._y_train[k] for k in range(m)])
        v = np.zeros(m)
        for i in range(m):
            ai = self.alpha_[i]
            r = self._y_train[i] * E[i]
            if ai < self.eps_alpha:
                v[i] = max(0.0, -r)
            elif ai > self.C - self.eps_alpha:
                v[i] = max(0.0, r)
            else:
                v[i] = abs(r)
        return v

    def support_vectors(self):
        sv_mask = self.alpha_ > 1e-4
        self.support_indices_ = np.nonzero(sv_mask)[0]
        self.support_vectors_ = self._X_train[sv_mask]
        self.support_labels_ = self._y_train[sv_mask]
        self.support_alpha_ = self.alpha_[sv_mask]

    @property
    def n_support_vectors_(self):
        if self.support_indices_ is not None:
            return int(len(self.support_indices_))
        else:
            return 0
    def weights_bias_linear(self):
        if self.kernel != "linear":
            raise RuntimeError("linear only")
        w = np.sum((self.alpha_ * self._y_train)[:, None] * self._X_train, axis=0)
        return w, float(self.b_)
