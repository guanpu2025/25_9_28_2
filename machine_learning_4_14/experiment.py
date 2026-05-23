import os
import urllib.request

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC

from smo_svm import SMOSVM


def total(sk):
    return int(np.sum(sk.n_support_))

def erD1000yangben(n=1000, noise=0.08, seed=42):
    rng = np.random.default_rng(seed)

    n1 = n // 2
    n2 = n - n1

    X1 = rng.normal(
        loc=[-1.2, -1.0],
        scale=[0.55, 0.45],
        size=(n1, 2)
    )

    X2 = rng.normal(
        loc=[1.0, 1.1],
        scale=[0.5, 0.5],
        size=(n2, 2)
    )

    X = np.vstack([X1, X2])

    X = np.vstack([X, [[-3.5, -3.0]]])

    y = np.hstack([
        -np.ones(n1),
        np.ones(n2),
        [1]
    ])

    if noise > 0:
        flip = rng.random(len(y)) < noise
        y[flip] *= -1

    perm = rng.permutation(len(y))

    return X[perm], y[perm]


'''def erD1000yangben(n=1000, noise=0.08, seed=42):
    rng = np.random.default_rng(seed)
    n1 = n // 2
    n2 = n - n1
    X1 = rng.normal(loc=[-1.2, -1.0], scale=[0.55, 0.45], size=(n1, 2))
    X2 = rng.normal(loc=[1.0, 1.1], scale=[0.5, 0.5], size=(n2, 2))
    X = np.vstack([X1, X2])
    X.append([-2, -2])
    y = np.hstack([-np.ones(n1), np.ones(n2)])
    y.append(1)
    if noise > 0:
        flip = rng.random(n) < noise
        y[flip] *= -1
    perm = rng.permutation(n)
    return X[perm], y[perm]
'''

def draw_2D_linear(X, y, model, title, out_path):
    w, b = model.weights_bias_linear()
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx = np.linspace(x_min, x_max, 200)

    def line_x2(x1, rhs):
        if abs(w[1]) < 1e-9:
            return None
        return (rhs - w[0] * x1 - b) / w[1]

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(X[y < 0, 0], X[y < 0, 1], c="#0062FF", s=14, label="y=-1", alpha=0.65)
    ax.scatter(X[y > 0, 0], X[y > 0, 1], c="#FF5E00", s=14, label="y=+1", alpha=0.65)
    for rhs, sty, lab in [(0, "k-", "decision"), (-1, "k--", "-1"), (1, "k--", "+1")]:
        yy = line_x2(xx, rhs)
        if yy is not None:
            ax.plot(xx, yy, sty, linewidth=1.4, label=lab)
    sv = model.support_vectors_
    if sv is not None and len(sv):
        ax.scatter(
            sv[:, 0],
            sv[:, 1],
            s=55,
            facecolors="none",
            edgecolors="green",
            linewidths=1.6,
            label="support",
        )
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title)
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def draw_2d_rbf(X, y, model, title, out_path, grid_n=180):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    gx = np.linspace(x_min, x_max, grid_n)
    gy = np.linspace(y_min, y_max, grid_n)
    GX, GY = np.meshgrid(gx, gy)
    G = np.c_[GX.ravel(), GY.ravel()]
    Z = model.decision_function(G).reshape(GX.shape)
    fig, ax = plt.subplots(figsize=(7, 6))
    cs = ax.contourf(GX, GY, Z, levels=30, cmap="coolwarm", alpha=0.55)
    ax.contour(GX, GY, Z, levels=[-1, 0, 1], colors="k", linestyles=["--", "-", "--"], linewidths=1.2)
    fig.colorbar(cs, ax=ax, fraction=0.046, pad=0.04)
    ax.scatter(X[y < 0, 0], X[y < 0, 1], c="#0095ff", s=12, label="y=-1", alpha=0.75)
    ax.scatter(X[y > 0, 0], X[y > 0, 1], c="#ff7700", s=12, label="y=+1", alpha=0.75)
    sv = model.support_vectors_
    if sv is not None and len(sv):
        ax.scatter(
            sv[:, 0],
            sv[:, 1],
            s=50,
            facecolors="none",
            edgecolors="lime",
            linewidths=1.4,
            label="support",
        )
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)
    ax.set_aspect("equal", adjustable="box")
    ax.set_title(title)
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def task2():
    print("二，二维1000样本")
    X, y = erD1000yangben(1000, noise=0.01, seed=66)
    C = 1.0
    tol = 1e-3
    base = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(base, "figures")
    os.makedirs(out_dir, exist_ok=True)

    m_lin = SMOSVM(C=C, kernel="linear", tol=tol, max_iter=5000, random_state=0)
    m_lin.fit(X, y)
    plt.plot(m_lin.kkt_history_, label="linear")
    print("线性核 迭代次数=%d 支持向量=%d 最大KKt违反=%.6g alpha*yi的和=%.3e" % (m_lin.n_iterations_, m_lin.n_support_vectors_, m_lin.max_kkt_violation_, m_lin.mean_abs_dual_eq_))
    draw_2D_linear(X, y, m_lin, "2Dlinear", os.path.join(out_dir, "task2_linear.png"))

    gamma = 0.7
    m_rbf = SMOSVM(C=C, kernel="rbf", gamma=gamma, tol=tol, max_iter=8000, random_state=1)
    m_rbf.fit(X, y)
    plt.plot(m_rbf.kkt_history_, label="rbf")
    print("rbf核 gamma=%s 迭代次数=%d 支持向量=%d 最大KKt违反=%.6g alpha*yi的和=%.3e" % (gamma, m_rbf.n_iterations_, m_rbf.n_support_vectors_, m_rbf.max_kkt_violation_, m_rbf.mean_abs_dual_eq_))
    draw_2d_rbf(X, y, m_rbf, "2DRBF", os.path.join(out_dir, "task2_rbf.png"))
    #print("Saved:", os.path.join(out_dir, "task2_linear.png"), os.path.join(out_dir, "task2_rbf.png"))
    os.path.join(out_dir, "task2_linear.png")
    os.path.join(out_dir, "task2_rbf.png")
    '''plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("Max KKT")
    plt.title("SMO")
    plt.legend()
    plt.grid()
    plt.show()'''

def getaustralian(dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    url = "https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary/australian_scale"
    fname = os.path.basename(url)
    path = os.path.join(dest_dir, fname)
    if not os.path.isfile(path):
        print("Downloading:", url)
        urllib.request.urlretrieve(url, path)
    return path


def loadfile(path):
    rows = []
    labels = []
    max_idx = 0
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            labels.append(float(parts[0]))
            feat = {}
            for p in parts[1:]:
                if ":" not in p:
                    continue
                k, v = p.split(":", 1)
                idx = int(k)
                feat[idx] = float(v)
                max_idx = max(max_idx, idx)
            rows.append(feat)
    n = len(labels)
    d = max_idx
    X = np.zeros((n, d), dtype=np.float64)
    for i, feat in enumerate(rows):
        for j, val in feat.items():
            X[i, j - 1] = val
    y = np.array(labels, dtype=np.float64)
    y[y == 0] = -1.0
    y[y > 0] = 1.0
    y[y < 0] = -1.0
    return X, y


def task3():
    print("三，australian上与sklearn的对比")
    base = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base, "data")
    path = getaustralian(data_dir)
    X, y = loadfile(path)
    scaler = MinMaxScaler()
    Xs = scaler.fit_transform(X)
    X_tr, X_te, y_tr, y_te = train_test_split(Xs, y, test_size=0.3, random_state=42, stratify=y)
    C = 1.0
    tol = 1e-3
    gamma = 1.0 / X_tr.shape[1]

    def report(name, model, sk):
        acc_tr = accuracy_score(y_tr, model.predict(X_tr))
        acc_te = accuracy_score(y_te, model.predict(X_te))
        sk_tr = accuracy_score(y_tr, sk.predict(X_tr))
        sk_te = accuracy_score(y_te, sk.predict(X_te))
        sk_sv = total(sk)
        print(
            "SMO 训练集=%.4f 测试集=%.4f 支持向量=%d 迭代次数=%d 最大KKT=%.6g alpha*yi的和=%.3e"
            % (acc_tr, acc_te, model.n_support_vectors_, model.n_iterations_, model.max_kkt_violation_, model.mean_abs_dual_eq_)
        )
        print("sklearn 训练集=%.4f 测试集=%.4f 支持向量=%d" % (sk_tr, sk_te, sk_sv))

    smo_lin = SMOSVM(C=C, kernel="linear", tol=tol, max_iter=2000, random_state=3)
    smo_lin.fit(X_tr, y_tr)
    sk_lin = SVC(C=C, kernel="linear", tol=tol)
    sk_lin.fit(X_tr, y_tr)
    report("linear", smo_lin, sk_lin)

    smo_rbf = SMOSVM(C=C, kernel="rbf", gamma=gamma, tol=tol, max_iter=2500, random_state=4)
    smo_rbf.fit(X_tr, y_tr)
    sk_rbf = SVC(C=C, kernel="rbf", gamma=gamma, tol=tol)
    sk_rbf.fit(X_tr, y_tr)
    report("rbf gamma=1/n", smo_rbf, sk_rbf)
    
    '''plt.plot(smo_lin.kkt_history_, label="linear")
    plt.plot(smo_rbf.kkt_history_, label="rbf")

    plt.yscale("log")
    plt.xlabel("Iteration")
    plt.ylabel("Max KKT violation")
    plt.title("SMO Convergence Curve")
    plt.legend()
    plt.grid()
    plt.show()'''


def task1():
    print("一，小数据集")
    rng = np.random.default_rng(0)
    X = rng.normal(size=(80, 2))
    y = np.sign(X[:, 0] + 0.3 * X[:, 1] - 0.1)
    y[y == 0] = 1.0
    m = SMOSVM(C=1.0, kernel="linear", tol=1e-3, max_iter=5000, random_state=0)
    m.fit(X, y)
    print("线性核 最大KKT违反量=%.6g 支持向量数=%d 迭代次数=%d" % (m.max_kkt_violation_, m.n_support_vectors_, m.n_iterations_))
    m2 = SMOSVM(C=1.0, kernel="rbf", gamma=0.5, tol=1e-3, max_iter=8000, random_state=1)
    m2.fit(X, y)
    print("rbf核 最大KKT违反量=%.6g 支持向量数=%d 迭代次数=%d" % (m2.max_kkt_violation_, m2.n_support_vectors_, m2.n_iterations_))


if __name__ == "__main__":
    task1()
    task2()
    task3()
    print("\n完成")
