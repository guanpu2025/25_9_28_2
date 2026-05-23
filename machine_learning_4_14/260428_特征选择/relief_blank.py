import numpy as np
import pandas as pd
from tqdm import tqdm


class Relief:
    """
    二分类 Relief 算法。

    输入:
        X: pandas DataFrame
           数值特征 dtype 为 float/int
           离散特征 dtype 为 category/object

        y: pandas Series
           二分类标签

    输出:
        每个特征的 Relief 统计量。
    """

    def __init__(self, sample_size=1000, random_state=42):
        self.sample_size = sample_size
        self.random_state = random_state

    def fit(self, X, y):
        # Step 1. 分离连续特征和离散特征
        num_cols = X.select_dtypes(include=["number"]).columns.tolist()
        cat_cols = X.select_dtypes(exclude=["number"]).columns.tolist()

        self.num_cols = num_cols
        self.cat_cols = cat_cols
        self.feature_names = num_cols + cat_cols

        # Step 2. 构造连续特征矩阵; 连续特征需要进行归一化
        X_num = X[num_cols].astype(float).copy()
        X_num = (X_num - X_num.min()) / (X_num.max() - X_num.min() + 1e-12)
        X_num = X_num.to_numpy()

        # Step 3. 构造离散特征矩阵; 将原始离散特征转换为离散数值编码
        X_cat = []
        for col in cat_cols:
            if str(X[col].dtype) == "category":
                codes = X[col].cat.codes.to_numpy()
            else:
                codes = pd.factorize(X[col])[0]
            X_cat.append(codes.reshape(-1, 1))
        X_cat = np.hstack(X_cat)

        # Step 4. 标签编码
        y = pd.factorize(y)[0]

        n_samples = X.shape[0]
        n_features = len(self.feature_names)
        scores = np.zeros(n_features)

        # Step 5. 随机抽取部分样本; 在数据集的采样上估计相关统计量
        rng = np.random.default_rng(self.random_state)
        sample_size = min(self.sample_size, n_samples)
        sample_idx = rng.choice(n_samples, size=sample_size, replace=False)

        for i in tqdm(sample_idx, desc="Relief: searching near-hit/miss for each sample"):
            # Step 6. 计算样本 xi 与所有样本在每个特征上的 diff。

            # TODO: 计算数值特征上的样本间距离：diff = |xi - xj|
            # diff_num.shape = [n_samples, n_num_features]
            diff_num = ...
            # TODO: 计算离散特征上的样本间距离：相同为 0，不同为 1
            # diff_cat.shape = [n_samples, n_cat_features]
            diff_cat = ...
            diff = np.hstack([diff_num, diff_cat])

            # Step 7. TODO: 计算样本 xi 到所有样本的距离。
            dist = ...
            dist[i] = np.inf

            # Step 8. TODO: 找 near-hit：同类最近邻的 index
            hit_idx = ...
            hit_idx = hit_idx[hit_idx != i]
            near_hit = ...

            # Step 9. TODO: 找 near-miss：异类最近邻的 index
            miss_idx = ...
            near_miss = ...

            # Step 10. 根据公式(11.3)更新每个特征的相关统计量
            scores += -diff[near_hit] ** 2 + diff[near_miss] ** 2

        # Step 11. 对采样次数取平均。
        self.scores = scores / sample_size

        self.ranking = (
            pd.DataFrame({
                "feature": self.feature_names,
                "score": self.scores
            })
            .sort_values("score", ascending=False)
            .reset_index(drop=True)
        )

        return self

    def get_ranking(self):
        return self.ranking

    def select_top_k(self, k):
        return self.ranking.head(k)["feature"].tolist()


if __name__ == "__main__":
    from bank_marketing import get_bank_marketing

    Xy, X, y = get_bank_marketing()

    selector = Relief(sample_size=1000, random_state=42)
    selector.fit(X, y)

    print("\nRelief 特征排序结果：")
    print(selector.get_ranking())

    print("\nTop-5 特征：")
    print(selector.select_top_k(5))